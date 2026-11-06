#!/usr/bin/env python3
"""SEO/AEO crawl check for every URL in a sitemap (stdlib only).

Usage:
  python3 seo_audit.py https://example.com/sitemap.xml
  python3 seo_audit.py https://example.com/sitemap.xml --map https://example.com=https://staging.example.com --insecure
Options: --limit N  --workers N  --json report.json
Exit code 1 when any Critical issue is found (use it as a CI gate).
"""
import argparse, concurrent.futures as cf, gzip, html, json, re, ssl, sys, urllib.error, urllib.request
from collections import Counter, defaultdict
from html.parser import HTMLParser

RETIRED = {'HowTo', 'SpecialAnnouncement', 'ClaimReview'}  # schema.org types whose Google rich results were retired
RTL = ('ar', 'he', 'fa', 'ur', 'ckb', 'ps', 'sd', 'ug', 'yi', 'dv')


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def build_opener(insecure):
    context = ssl.create_default_context()
    if insecure:
        context.check_hostname, context.verify_mode = False, ssl.CERT_NONE
    return urllib.request.build_opener(NoRedirect, urllib.request.HTTPSHandler(context=context))


def header_map(message):
    return {key.lower(): ', '.join(message.get_all(key) or []) for key in set(message.keys())}


def decode(raw, charset):
    if raw[:2] == b'\x1f\x8b':
        raw = gzip.decompress(raw)
    try:
        return raw.decode(charset or 'utf-8', 'replace')
    except LookupError:
        return raw.decode('utf-8', 'replace')


def fetch(opener, url):
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; seo-audit/1.0)'})
    try:
        response = opener.open(request, timeout=60)
        return response.status, header_map(response.headers), decode(response.read(), response.headers.get_content_charset())
    except urllib.error.HTTPError as error:
        return error.code, header_map(error.headers), ''
    except Exception as error:
        return 'ERR ' + str(error)[:60], {}, ''


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.page = {'title': '', 'h1': 0, 'canonical': [], 'robots': '', 'description': None, 'alternates': {},
                     'jsonld': [], 'og': {}, 'images': 0, 'no_alt': 0, 'no_size': 0, 'lang': None, 'dir': None}
        self.capture, self.buffer, self.svg_depth = None, '', 0

    def handle_starttag(self, tag, attrs):
        a, p = dict(attrs), self.page
        rel = (a.get('rel') or '').lower()
        if tag == 'svg':
            self.svg_depth += 1
        if tag == 'html':
            p['lang'], p['dir'] = (a.get('lang') or '').lower(), (a.get('dir') or '').lower()
        elif (tag == 'title' and not self.svg_depth and not p['title']) or \
                (tag == 'script' and (a.get('type') or '').split(';')[0].strip().lower() == 'application/ld+json'):
            self.capture, self.buffer = tag, ''
        elif tag == 'h1':
            p['h1'] += 1
        elif tag == 'link' and rel == 'canonical':
            p['canonical'].append(a.get('href'))
        elif tag == 'link' and rel == 'alternate' and a.get('hreflang'):
            p['alternates'][a['hreflang'].lower()] = a.get('href')
        elif tag == 'meta':
            name, prop = (a.get('name') or '').lower(), (a.get('property') or '').lower()
            key = prop or name
            if name == 'description':
                p['description'] = a.get('content') or ''
            elif name == 'robots':
                p['robots'] = (a.get('content') or '').lower()
            elif key.startswith(('og:', 'twitter:')):
                p['og'][key] = a.get('content')
        elif tag == 'img':
            p['images'] += 1
            p['no_alt'] += a.get('alt') is None
            p['no_size'] += not (a.get('width') and a.get('height'))

    def handle_data(self, data):
        if self.capture:
            self.buffer += data

    def handle_endtag(self, tag):
        if tag == 'svg' and self.svg_depth:
            self.svg_depth -= 1
        if self.capture == 'title' and tag == 'title':
            self.page['title'], self.capture = self.buffer.strip(), None
        elif self.capture == 'script' and tag == 'script':
            self.page['jsonld'].append(self.buffer)
            self.capture = None


def schema_types(node):
    if isinstance(node, list):
        return [t for item in node for t in schema_types(item)]
    if isinstance(node, dict):
        found = node.get('@type', [])
        found = found if isinstance(found, list) else [found]
        return found + [t for value in node.values() for t in schema_types(value)]
    return []


def sitemap_urls(opener, url, remap):
    status, _, body = fetch(opener, remap(url))
    if status != 200:
        sys.exit(f'Sitemap {url} returned {status}')
    locs = [html.unescape(loc) for loc in re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', body)]
    if '<sitemapindex' in body:
        return [u for child in locs for u in sitemap_urls(opener, child, remap)]
    return locs


def audit(opener, url, remap, unmap):
    status, headers, body = fetch(opener, remap(url))
    issues = []
    add = lambda severity, text: issues.append((severity, text))
    if status != 200:
        add('C', f'status {status} (sitemap URLs must return 200)')
        return {'url': url, 'issues': issues, 'alternates': {}, 'title': '', 'description': ''}
    parser = PageParser()
    parser.feed(body)
    p = parser.page
    p['canonical'] = [unmap(c or '') for c in p['canonical']]
    p['alternates'] = {lang: unmap(href or '') for lang, href in p['alternates'].items()}
    if 'noindex' in p['robots'] or 'noindex' in headers.get('x-robots-tag', '').lower():
        add('H', 'noindex URL listed in sitemap')
    if not p['title']:
        add('C', 'missing <title>')
    elif not 30 <= len(p['title']) <= 60:
        add('M', f'title length {len(p["title"])} (30-60; Arabic ~45-55)')
    low, high = (110, 140) if (p['lang'] or '').split('-')[0] in RTL else (120, 160)
    if p['description'] is None:
        add('H', 'missing meta description')
    elif not low <= len(p['description']) <= high:
        add('L', f'description length {len(p["description"])} ({low}-{high})')
    if p['h1'] != 1:
        add('M', f'{p["h1"]} <h1> elements (need exactly 1)')
    if len(p['canonical']) != 1:
        add('H', f'{len(p["canonical"])} canonical tags (need exactly 1)')
    elif p['canonical'][0] != url:
        add('H', f'canonical {p["canonical"][0]} is not this URL')
    if p['alternates']:
        if url not in p['alternates'].values():
            add('C', 'hreflang set has no self-reference')
        if 'x-default' not in p['alternates']:
            add('M', 'hreflang set has no x-default')
    if not p['lang']:
        add('H', 'missing <html lang>')
    elif p['lang'].split('-')[0] in RTL and p['dir'] != 'rtl':
        add('H', f'lang={p["lang"]} without dir="rtl"')
    if not p['jsonld']:
        add('M', 'no JSON-LD')
    found_types = set()
    for block in p['jsonld']:
        try:
            data = json.loads(block)
        except ValueError:
            add('C', 'invalid JSON-LD')
            continue
        found_types.update(str(t) for t in schema_types(data))
        roots = data if isinstance(data, list) else [data]
        if any(isinstance(r, dict) and 'schema.org' not in str(r.get('@context', '')) for r in roots):
            add('H', 'JSON-LD block without schema.org @context')
    for retired in sorted(found_types & RETIRED):
        add('L', f'schema type {retired} no longer produces a Google rich result')
    for key in ('og:title', 'og:description', 'og:image', 'twitter:card'):
        if not p['og'].get(key):
            add('L', f'missing {key}')
    if p['no_alt']:
        add('M', f'{p["no_alt"]} <img> without alt')
    if p['no_size']:
        add('L', f'{p["no_size"]} <img> without width/height')
    if len(body.encode()) > 2_000_000:
        add('H', 'HTML larger than 2 MB')
    return {'url': url, 'issues': issues, 'alternates': p['alternates'], 'title': p['title'], 'description': p['description'] or ''}


def main():
    cli = argparse.ArgumentParser(description='SEO/AEO crawl check')
    cli.add_argument('sitemap')
    cli.add_argument('--map', help='rewrite URLs before fetching: https://prod=https://staging')
    cli.add_argument('--insecure', action='store_true', help='skip TLS verification (local/staging)')
    cli.add_argument('--limit', type=int, default=0)
    cli.add_argument('--workers', type=int, default=6)
    cli.add_argument('--json', help='write the full report to this file')
    args = cli.parse_args()
    source, target = (args.map.split('=', 1) + [''])[:2] if args.map else ('', '')
    remap = (lambda u: u.replace(source, target, 1)) if source else (lambda u: u)
    unmap = (lambda u: u.replace(target, source, 1)) if source else (lambda u: u)
    opener = build_opener(args.insecure)

    urls = list(dict.fromkeys(sitemap_urls(opener, args.sitemap, remap)))
    urls = urls[:args.limit] if args.limit else urls
    if not urls:
        sys.exit('No URLs found in the sitemap')
    with cf.ThreadPoolExecutor(args.workers) as pool:
        pages = list(pool.map(lambda u: audit(opener, u, remap, unmap), urls))

    by_url = {page['url']: page for page in pages}
    for page in pages:
        for lang, href in page['alternates'].items():
            if lang == 'x-default' or href == page['url']:
                continue
            target_page = by_url.get(href)
            if target_page is None:
                page['issues'].append(('M', f'hreflang {lang} -> {href} is not in the sitemap'))
            elif target_page['alternates'] and page['url'] not in target_page['alternates'].values():
                page['issues'].append(('C', f'hreflang {lang} -> {href} has no return link'))
    for field in ('title', 'description'):
        groups = defaultdict(list)
        for page in pages:
            if page[field]:
                groups[page[field]].append(page)
        for duplicates in (g for g in groups.values() if len(g) > 1):
            for page in duplicates:
                page['issues'].append(('M', f'duplicate {field} ({len(duplicates)} pages)'))

    counts = Counter((severity, re.sub(r'(?<![A-Za-z])\d+|https?://\S+', '#', text)) for page in pages for severity, text in page['issues'])
    order = {'C': 0, 'H': 1, 'M': 2, 'L': 3}
    print(f'Checked {len(pages)} URLs\n')
    print(f'{"Sev":<4}{"Pages":>6}  Issue')
    for (severity, text), count in sorted(counts.items(), key=lambda item: (order[item[0][0]], -item[1])):
        print(f'{severity:<4}{count:>6}  {text}')
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as handle:
            json.dump(pages, handle, ensure_ascii=False, indent=1)
    critical = sum(1 for page in pages for severity, _ in page['issues'] if severity == 'C')
    print(f'\nCritical issues: {critical}')
    sys.exit(1 if critical else 0)


if __name__ == '__main__':
    main()
