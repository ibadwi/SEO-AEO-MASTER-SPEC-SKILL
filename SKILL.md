---
name: seo-aeo-master-spec
description: Implement or audit technical SEO and answer engine optimization on websites, including metadata, indexing, sitemaps, structured data, multilingual hreflang, Arabic RTL, content architecture and AI search readiness. Use when asked to improve search visibility or review SEO/AEO compliance.
---

# SEO + AEO Master Spec

Read [SEO-AEO-MASTER-SPEC.md](SEO-AEO-MASTER-SPEC.md), starting with Start here and §0. Select the applicable sections before implementation. Load the detailed sections relevant to the site; use §35 as the audit blueprint and §37 for completion criteria.

1. Establish scope: a URL-only or review request means audit mode; change no site code. For implementation, inspect the repository, stack, routes, templates, languages and existing rules first.
2. Preserve existing behavior and real content. Never invent reviews, statistics, dates, credentials or business facts.
3. Apply only relevant requirements, marking others not applicable with reasons. Preserve the bilingual English/Arabic pairing and section numbering when changing this specification.
4. For authorized crawl checks, run `python3 scripts/seo_audit.py https://example.com/sitemap.xml --workers 2 --rate 2 --json report.json`. Respect robots.txt and scope; the script does not enforce robots.txt itself. Keep TLS verification enabled.
5. Validate changes with the project’s relevant checks and §30. The crawler is a limited static HTML check, not proof of full SEO/AEO compliance. Verify time-sensitive engine rules against the primary sources listed in §34.
6. Deliver evidence, affected files, critical findings, priorities and unverified items. In audit mode follow the §35.7 report and §31 scoring; do not infer unmeasured scores from tag presence or promise rankings or AI citations.

## العربية

اقرأ المواصفة المرفقة بدءًا من «ابدأ من هنا» و§0، وحدد الأقسام المنطبقة. استخدم §35 للتدقيق و§37 لمعايير الإنجاز. طلب المراجعة أو الرابط وحده يعني التدقيق دون تعديل الموقع. قبل التنفيذ افحص المشروع وتقنياته وقواعده. لا تختلق بيانات، وحافظ على تزامن اللغتين وترقيم الأقسام. افحص الروابط المصرح بها فقط واحترم robots.txt؛ السكربت لا يفرضه تلقائيًا. تحقّق من النتائج واذكر الأدلة والقيود وما لم يُختبر؛ لا تَعِد بترتيب أو اقتباسات.
