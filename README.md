# SEO + AEO Master Spec · المواصفة الشاملة لتحسين محركات البحث والإجابة

**English** · [العربية](#بالعربية)

An open, bilingual (English + Arabic) specification that AI coding agents and humans can follow to **implement** or **audit** search engine optimization (SEO) and answer engine optimization (AEO) on any website: technical SEO, content, structured data, Arabic/RTL and every language, AI search engines, off-site authority, migrations, privacy, templates, verification and scoring.

- One file, [`SEO-AEO-MASTER-SPEC.md`](SEO-AEO-MASTER-SPEC.md): every requirement in English with its Arabic version directly under it, one checkbox per requirement, severity tags `[C]` `[H]` `[M]` `[L]` `[I]`.
- **Audit mode** (§0) and a **site blueprint** (§35): the pages, page sections, root files, head tags, HTTP settings and platform settings every website should have — so any site can be reviewed and told exactly what is missing or wrong.
- A dependency-free crawl script, [`scripts/seo_audit.py`](scripts/seo_audit.py), that checks every URL in a sitemap and fails CI on critical issues.

## What's inside

| Part | Sections |
|---|---|
| Start here | Which sections apply to your site, the 20 first-week actions |
| Foundations | §0 execution protocol (implement & audit modes) · §1–§12 crawling, indexing, rendering, security, URLs, mobile, Core Web Vitals, on-page, sitemaps, hreflang, images, structured data |
| Content & architecture | §13 E-E-A-T and content quality · §14 clusters, page types, programmatic and comparison pages |
| Site types | §15 local · §16 e-commerce · §17 AI agent readiness (llms.txt, accessibility) |
| Languages | §20 Arabic & RTL · §21 all languages and scripts |
| AEO | §22 answer engine optimization · §23 off-site authority & entity building · §24 per-engine notes and share of voice |
| Lifecycle | §18 release regression · §19 measurement · §25 migrations · §26 Discover, News, shopping, video, social search · §27 privacy & consent |
| Toolkit | §28 page templates · §29 framework recipes (Laravel, Next.js, Nuxt, WordPress, Astro, SvelteKit, React Router, SPA, static) · §30 verification kit · §31 SEO & AEO scoring · §32 operations & governance |
| Audit & reference | §33 glossary · §34 maintenance · §35 site blueprint (essential pages, page sections, root files, head tags, HTTP, platform settings, audit report) · §36 special cases (SaaS, faceted navigation, expired content, PDFs, UGC, subdomains, apps) · §37 definition of done |

## How to use

**With an AI coding agent (Claude Code, Cursor, GitHub Copilot, Codex, Windsurf, …)**

1. Copy `SEO-AEO-MASTER-SPEC.md` into your project, for example `docs/seo/`.
2. Optionally point your agent instructions file (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`, …) at it:
   ```text
   For any SEO, AEO, metadata, sitemap, schema or content-structure work, follow docs/seo/SEO-AEO-MASTER-SPEC.md.
   ```
3. Ask, in English or Arabic:
   - Implement: `Implement docs/seo/SEO-AEO-MASTER-SPEC.md in full.` · `نفّذ docs/seo/SEO-AEO-MASTER-SPEC.md بالكامل`
   - Audit only: `Audit https://example.com with docs/seo/SEO-AEO-MASTER-SPEC.md (audit mode) and give me the §35.7 report and §31 scores.` · `دقّق الموقع https://example.com وفق المواصفة (وضع التدقيق) وأعطني تقرير §35.7 ودرجات §31`

**By hand:** start with *Start here*, then work through the sections that apply, tick the checkboxes, and use §30 to verify.

## Crawl script

```bash
python3 scripts/seo_audit.py https://example.com/sitemap.xml
python3 scripts/seo_audit.py https://example.com/sitemap.xml --map https://example.com=https://staging.example.com --insecure --json report.json
```

Python 3.9+, standard library only. Checks status, title, description, H1, canonical, hreflang (self, x-default, return links), `lang`/`dir`, JSON-LD validity and deprecated types, Open Graph/Twitter, images, HTML size and duplicates. Exit code `1` when any Critical issue exists. Use `--workers 2` or lower on sites you don't own.

## Principles

- **No invented data** — no placeholders, fake reviews, fake dates or made-up statistics.
- **Honest claims** — nothing here promises rankings, traffic or AI citations.
- **Primary sources win** — heuristics are labeled as such; official documentation is the reference (§34.2).
- **Both languages stay in sync** — every change is made in English and Arabic.

## Contributing

Corrections and additions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Search and AI-engine rules change often; a correction with a primary source is the most valuable contribution.

## Credits & license

MIT — see [LICENSE](LICENSE). The original audit knowledge base was derived from [claude-seo](https://github.com/AgriciDaniel/claude-seo) by AgriciDaniel (MIT); this project reorganizes it into an implementation spec and extends it.

**Disclaimer:** guidance, not a guarantee. Not legal advice (see §27). Verify time-sensitive facts against the official sources before acting.

---

## بالعربية

مواصفة مفتوحة المصدر ثنائية اللغة (عربي + إنجليزي) يتبعها وكلاء البرمجة بالذكاء الاصطناعي والبشر **لتنفيذ** أو **تدقيق** تحسين محركات البحث (SEO) وتحسين محركات الإجابة (AEO) في أي موقع: السيو التقني، والمحتوى، والبيانات المنظمة، والعربية وRTL وكل اللغات، ومحركات البحث بالذكاء الاصطناعي، والسلطة خارج الموقع، ونقل المواقع، والخصوصية، والقوالب، والتحقق، والدرجات.

- ملف واحد [`SEO-AEO-MASTER-SPEC.md`](SEO-AEO-MASTER-SPEC.md): كل متطلب بالإنجليزية وتحته مباشرة النسخة العربية، ومربع اختيار واحد لكل متطلب، ووسوم خطورة `[C]` `[H]` `[M]` `[L]` `[I]`.
- **وضع التدقيق** (§0) و**مخطط الموقع** (§35): الصفحات وأقسام الصفحات وملفات الجذر ووسوم head وإعدادات HTTP والمنصات التي يحتاجها كل موقع — لمراجعة أي موقع وإخباره بدقة بما ينقصه أو ما هو خاطئ.
- سكربت فحص بلا اعتماديات [`scripts/seo_audit.py`](scripts/seo_audit.py) يفحص كل روابط خريطة الموقع ويُفشل CI عند المشكلات الحرجة.

### طريقة الاستخدام

**مع وكيل برمجة بالذكاء الاصطناعي (Claude Code أو Cursor أو GitHub Copilot أو Codex أو Windsurf…):**

1. انسخ `SEO-AEO-MASTER-SPEC.md` إلى مشروعك، مثلاً في `docs/seo/`.
2. اختيارياً، أشر إليه في ملف تعليمات الوكيل (`CLAUDE.md` أو `AGENTS.md` أو `.cursorrules`…).
3. اطلب بالعربية أو الإنجليزية:
   - للتنفيذ: `نفّذ docs/seo/SEO-AEO-MASTER-SPEC.md بالكامل`
   - للتدقيق فقط: `دقّق الموقع https://example.com وفق المواصفة (وضع التدقيق) وأعطني تقرير §35.7 ودرجات §31`

**يدوياً:** ابدأ بقسم *ابدأ من هنا*، ثم اعمل على الأقسام المنطبقة، وعلّم المربعات، واستخدم §30 للتحقق.

### المبادئ
- **لا بيانات مختلقة** — لا نصوص مؤقتة ولا مراجعات أو تواريخ أو إحصاءات مزيفة.
- **ادعاءات صادقة** — لا شيء هنا يَعِد بترتيب أو زيارات أو اقتباس من الذكاء الاصطناعي.
- **المصدر الرسمي هو المرجع** — والإرشادات غير الرسمية معلَّمة بذلك (§34.2).
- **اللغتان متزامنتان دائماً** — كل تعديل يُكتب بالعربية والإنجليزية.

### المساهمة والترخيص
المساهمات مرحب بها — راجع [CONTRIBUTING.md](CONTRIBUTING.md). الترخيص MIT — راجع [LICENSE](LICENSE). المعرفة الأساسية مستخلصة من مشروع [claude-seo](https://github.com/AgriciDaniel/claude-seo) لـ AgriciDaniel (MIT)، وأُعيد تنظيمها ووُسّعت هنا.

**تنبيه:** إرشادات وليست ضماناً، وليست استشارة قانونية. تحقق من المعلومات المرتبطة بالوقت من المصادر الرسمية قبل التنفيذ.
