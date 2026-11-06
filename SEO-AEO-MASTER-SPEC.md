# SEO + AEO Master Spec · المواصفة الشاملة لتحسين محركات البحث والإجابة

> **EN:** One open, bilingual implementation and audit spec for technical SEO, content, structured data, Arabic/RTL, all languages and scripts, and AEO (Answer Engine Optimization) / LLM optimization. Drop it into any web project and ask: `Implement docs/seo/SEO-AEO-MASTER-SPEC.md in full`.
>
> **AR:** مواصفة مفتوحة ثنائية اللغة للتنفيذ والتدقيق تغطي السيو التقني، والمحتوى، والبيانات المنظمة، والعربية وRTL، وكل اللغات والأنظمة الكتابية، وتحسين محركات الإجابة AEO وتحسين الظهور في نماذج الذكاء الاصطناعي. ضعها في أي مشروع ويب ثم اطلب: `نفّذ docs/seo/SEO-AEO-MASTER-SPEC.md بالكامل`.

**Start with · ابدأ بـ:** the *Start here* section (which sections apply + the first-week 20 actions); to review an existing site, use **audit mode** (§0) and the **site blueprint** (§35) · قسم *ابدأ من هنا* (الأقسام المنطبقة وأهم 20 إجراء في الأسبوع الأول)؛ ولمراجعة موقع قائم استخدم **وضع التدقيق** (§0) و**مخطط الموقع** (§35).

**How to read · طريقة القراءة:** every item is written in English first, with the Arabic version directly under it. Each requirement has **one** checkbox. Severity tags: **[C]** Critical · **[H]** High · **[M]** Medium · **[L]** Low · **[I]** Info.
كل بند مكتوب بالإنجليزية أولاً وتحته مباشرة النسخة العربية، ولكل متطلب مربع اختيار **واحد** فقط. وسوم الخطورة: **[C]** حرج · **[H]** عالٍ · **[M]** متوسط · **[L]** منخفض · **[I]** معلومة.

**Source & credits · المصدر والشكر:** built on the audit knowledge base of [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) (MIT), reorganized into an implementation spec and extended. Facts and dates last verified 2026-11 (§34); numeric thresholds are *heuristics* unless marked as an engine rule.
مبنية على قاعدة معرفة مشروع claude-seo (رخصة MIT)، وأُعيد تنظيمها كمواصفة تنفيذ ووُسّعت. آخر تحقق من الحقائق والتواريخ في 2026-11 (§34)؛ والحدود الرقمية *إرشادية* ما لم يُذكر أنها قاعدة من المحرك.

---

## Start here · ابدأ من هنا

### S.1 Which sections apply · أي الأقسام تنطبق

| If the site… · إذا كان الموقع… | Apply · طبّق |
|---|---|
| Any website<br>أي موقع | §0–§9, §11–§13, §14.1–§14.2, §14.4, §17–§19, §22–§24, §27–§37 |
| Has more than one language<br>بأكثر من لغة | + §10, §21 |
| Has Arabic / Hebrew / Persian / Urdu pages<br>فيه صفحات عربية أو عبرية أو فارسية أو أردية | + §20 |
| Has a physical location or service area<br>له موقع فعلي أو منطقة خدمة | + §15 |
| Sells products online<br>يبيع منتجات | + §16, §26.3 (shopping surfaces) |
| Publishes news or frequent articles<br>ينشر أخباراً أو مقالات باستمرار | + §26.1–§26.2 |
| Publishes video or is active on social platforms<br>ينشر فيديو أو نشط على المنصات الاجتماعية | + §26.4–§26.5 |
| Is changing domain, platform, URLs or design<br>ينتقل لنطاق أو منصة أو روابط أو تصميم جديد | + §25 **before** anything else<br>+ §25 **قبل** أي شيء آخر |
| Generates pages from data at scale<br>يولّد صفحات من بيانات بأعداد كبيرة | + §14.3 |

### S.2 First week: the 20 highest-impact actions · الأسبوع الأول: أهم 20 إجراء

1. Crawl the whole site with the §30 kit, run the §35 blueprint audit, and save both as the baseline.
   - افحص الموقع كاملاً بأدوات §30، ونفّذ تدقيق مخطط الموقع §35، واحفظ النتيجتين كخط أساس.
2. Fix anything blocking indexing: `robots.txt` disallow-all, stray `noindex`, 5xx, broken canonicals (§1–§2).
   - أصلح كل ما يمنع الفهرسة: حظر شامل في `robots.txt`، `noindex` عرضي، أخطاء 5xx، canonical خاطئ (§1–§2).
3. Make sure titles, descriptions, canonicals, hreflang, JSON-LD and main text are in the server HTML (§3).
   - تأكد أن العناوين والأوصاف وcanonical وhreflang وJSON-LD والنص الأساسي موجودة في HTML الخادم (§3).
4. Force HTTPS and one host with single-hop 301s (§2, §4).
   - افرض HTTPS ونطاقاً واحداً بتحويل 301 من قفزة واحدة (§2، §4).
5. Generate the sitemap from real indexable URLs with real `lastmod`, and declare it in robots.txt (§9).
   - ولّد خريطة الموقع من الروابط الحقيقية القابلة للفهرسة بتاريخ تعديل حقيقي، وأعلنها في robots.txt (§9).
6. Decide the AI crawler policy with the owner and write robots.txt groups accordingly (§1.1).
   - قرّر سياسة زواحف الذكاء الاصطناعي مع المالك واكتب مجموعات robots.txt بناءً عليها (§1.1).
7. Build the central SEO head component; give every page a unique title, description and one H1 (§8).
   - ابنِ مكوّن SEO مركزياً؛ وأعطِ كل صفحة عنواناً ووصفاً فريدين وH1 واحداً (§8).
8. Fix hreflang: self-reference, reciprocity, `x-default` (§10).
   - أصلح hreflang: الإشارة للذات، والتبادلية، و`x-default` (§10).
9. Add the site-wide JSON-LD graph (Organization, WebSite, WebPage, BreadcrumbList) and stop relying on schema types whose Google rich results were retired (§12.2).
   - أضف مخطط JSON-LD العام (Organization وWebSite وWebPage وBreadcrumbList) وتوقّف عن الاعتماد على الأنواع التي أوقفت Google نتائجها المنسّقة (§12.2).
10. Fix the LCP image, image dimensions and render-blocking scripts on the top templates (§7, §11).
    - أصلح صورة LCP وأبعاد الصور والسكربتات المعطِّلة للعرض في أهم القوالب (§7، §11).
11. Verify the site in Google Search Console and Bing Webmaster Tools, submit sitemaps, enable IndexNow (§19, §24).
    - وثّق الموقع في Google Search Console وBing Webmaster Tools، وأرسل خرائط الموقع، وفعّل IndexNow (§19، §24).
12. Set up AI-referral tracking and a privacy-compliant analytics setup (§22.9, §27).
    - اضبط تتبّع الإحالات من الذكاء الاصطناعي وأداة تحليلات متوافقة مع الخصوصية (§22.9، §27).
13. Publish or fix About, Contact, Privacy, Terms and author pages (§13.1).
    - انشر أو أصلح صفحات من نحن، والتواصل، والخصوصية، والشروط، والكتّاب (§13.1).
14. Publish the "facts about the brand" page in every language (§22.3, template in §28).
    - انشر صفحة "حقائق عن العلامة" بكل لغة (§22.3، والقالب في §28).
15. Build the question bank for the top 3 topics in every language (§22.1).
    - ابنِ بنك الأسئلة لأهم 3 مواضيع بكل لغة (§22.1).
16. Rewrite the top 10 pages with the answer-block pattern (§22.2, template in §28).
    - أعد كتابة أهم 10 صفحات بنمط كتلة الإجابة (§22.2، والقالب في §28).
17. Make brand profiles consistent everywhere and link them with `sameAs` (§22.4, §23).
    - وحّد حسابات العلامة في كل مكان واربطها بـ `sameAs` (§22.4، §23).
18. Run the monthly AI share-of-voice prompt test once to get a baseline (§24.3).
    - شغّل اختبار نسبة الظهور في إجابات الذكاء الاصطناعي مرة واحدة لأخذ خط أساس (§24.3).
19. Add SEO checks to CI so regressions fail the build (§32.1).
    - أضف فحوص SEO إلى CI حتى يفشل البناء عند أي تراجع (§32.1).
20. Calculate the SEO and AEO scores (§31) and plan the next 90 days from the lowest categories.
    - احسب درجتي SEO وAEO (§31) وخطط للتسعين يوماً القادمة بدءاً من أضعف الفئات.

---

## 0. Execution protocol (read first — instructions for the coding agent) · بروتوكول التنفيذ (اقرأه أولاً — تعليمات لوكيل البرمجة)

You are implementing this spec in the current repository. Work through it end to end; do not just report.

أنت تطبّق هذه المواصفة على المستودع الحالي. نفّذها من البداية للنهاية؛ لا تكتفِ بكتابة تقرير.

**Two modes · وضعان:**

- **Implement mode** (you have the repository): follow steps 1–11 below.
  - **وضع التنفيذ** (لديك المستودع): اتبع الخطوات 1–11 أدناه.
- **Audit mode** (you only have a URL, or the owner asked for a review only): change nothing. Run the §35 blueprint audit, the §30 checks and crawl script, and score with §31; deliver the §35.7 report, both scores and the top 10 actions. On sites you don't own: no form submissions, no logins, no bypassing protections, respect robots.txt and keep to ≤ 2 requests/second (`--workers 2`).
  - **وضع التدقيق** (لديك رابط فقط، أو طلب المالك مراجعة فقط): لا تغيّر شيئاً. نفّذ تدقيق مخطط الموقع §35، وفحوص §30 وسكربت الفحص، واحسب الدرجات وفق §31؛ وسلّم تقرير §35.7 والدرجتين وأهم 10 إجراءات. وفي المواقع التي لا تملكها: لا إرسال نماذج، ولا تسجيل دخول، ولا تجاوز للحماية، واحترم robots.txt ولا تتجاوز طلبين في الثانية (`--workers 2`).

1. **Discover the stack.** Identify framework, templating layer (layouts, head partials), routing, how pages/content are stored (DB models, markdown, CMS), i18n setup, server config (nginx/.htaccess/middleware), build pipeline, and the project's own conventions (CLAUDE.md, design system, lint/format). Follow those conventions over anything generic here.
   - **اكتشف البنية التقنية.** حدّد إطار العمل، وطبقة القوالب (القوالب الرئيسية وأجزاء `<head>`)، والتوجيه (routing)، وطريقة تخزين الصفحات والمحتوى (نماذج قاعدة البيانات، markdown، نظام إدارة محتوى)، وإعداد تعدد اللغات، وإعدادات الخادم (nginx/.htaccess/middleware)، وخط البناء، وأعراف المشروع نفسه (CLAUDE.md، نظام التصميم، أدوات التنسيق). اتبع أعراف المشروع قبل أي شيء عام هنا.
2. **Classify the site** (can be several): SaaS, Local service, E-commerce, Publisher/blog, Agency, Tool. Also list every **locale** (language, region, script, direction) the site serves — §20 (Arabic/RTL) and §21 (all languages/scripts) apply per locale, and §22 (AEO) applies to every locale. Mark which sections below are *conditional* and skip those that do not apply (say so in the report).
   - **صنّف الموقع** (قد يكون أكثر من نوع): SaaS، خدمة محلية، متجر إلكتروني، ناشر/مدونة، وكالة، أداة. واذكر أيضاً كل **لغة/منطقة** يخدمها الموقع (اللغة، المنطقة، النظام الكتابي، الاتجاه) — §20 (العربية/RTL) و§21 (كل اللغات) تنطبقان على كل لغة، و§22 (AEO) تنطبق على كل لغة. حدّد الأقسام *المشروطة* وتجاوز ما لا ينطبق (واذكر ذلك في التقرير).
3. **Audit before editing.** For each section, list current state vs. requirement as a table: `item | status (pass/fail/n.a.) | severity | file(s)`.
   - **دقّق قبل التعديل.** لكل قسم، اعرض الحالة الحالية مقابل المطلوب في جدول: `البند | الحالة (ناجح/فاشل/لا ينطبق) | الخطورة | الملفات`.
4. **Fix in priority order:** Critical → High → Medium → Low. Severity meanings:
   - **أصلح حسب الأولوية:** حرج ← عالٍ ← متوسط ← منخفض. معاني الخطورة:
   - **[C] Critical** — blocks indexing or causes penalties. Fix now.
     - **[C] حرج** — يمنع الفهرسة أو يسبب عقوبات. أصلحه فوراً.
   - **[H] High** — significantly impacts rankings.
     - **[H] عالٍ** — يؤثر بشكل كبير على الترتيب.
   - **[M] Medium** — optimization opportunity.
     - **[M] متوسط** — فرصة تحسين.
   - **[L] Low / [I] Info** — backlog / optional.
     - **[L] منخفض / [I] معلومة** — لاحقاً / اختياري.
5. **Implement centrally.** Prefer one reusable SEO head component/service (title, meta, canonical, robots, hreflang, OG/Twitter, JSON-LD) fed by per-page data, rather than per-page copy-paste. Generate sitemap, robots.txt and llms.txt dynamically from real routes/data.
   - **نفّذ مركزياً.** فضّل مكوّناً/خدمة SEO واحدة قابلة لإعادة الاستخدام لعناصر `<head>` (العنوان، الوصف، canonical، robots، hreflang، OG/Twitter، JSON-LD) تتغذى من بيانات كل صفحة، بدل النسخ واللصق في كل صفحة. ولّد sitemap وrobots.txt وllms.txt ديناميكياً من المسارات والبيانات الحقيقية.
6. **Never invent data.** No placeholder text in shipped markup (`[Business Name]`, `REPLACE`, fake ratings, fake dates, fake reviews). If a real value is unknown (phone, address, social profiles, AI-training policy), collect all such questions and ask the owner once.
   - **لا تختلق بيانات أبداً.** لا نصوص مؤقتة في الكود المنشور (`[Business Name]`، `REPLACE`، تقييمات وهمية، تواريخ وهمية، مراجعات مزيفة). إن كانت قيمة حقيقية مجهولة (الهاتف، العنوان، حسابات التواصل، سياسة تدريب الذكاء الاصطناعي)، اجمع كل هذه الأسئلة واسأل المالك مرة واحدة.
7. **Test everything you change.** Add automated tests (feature/integration) asserting: status codes, presence/uniqueness of title/meta/H1/canonical, valid JSON-LD (parseable, `@context`, `@type`, no retired rich-result types), sitemap validity, robots.txt content, hreflang reciprocity, redirects. Run them.
   - **اختبر كل ما تغيّره.** أضف اختبارات آلية (feature/integration) تتحقق من: رموز الحالة، وجود وتفرّد العنوان/الوصف/H1/canonical، صلاحية JSON-LD (قابل للتحليل، `@context`، `@type`، بلا أنواع أُوقفت نتائجها المنسّقة)، صلاحية خريطة الموقع، محتوى robots.txt، تبادلية hreflang، التحويلات. وشغّلها.
8. **Report** at the end: what was fixed, what was skipped (and why), what needs owner input, and what can only be verified in production (CWV field data, Search Console).
   - **التقرير** في النهاية: ما أُصلح، وما تم تجاوزه (ولماذا)، وما يحتاج إلى مدخلات المالك، وما لا يمكن التحقق منه إلا في بيئة الإنتاج (بيانات CWV الميدانية، Search Console).
9. **Honest claims only.** Never promise rankings, traffic or AI citations in generated copy or docs.
   - **ادعاءات صادقة فقط.** لا تَعِد أبداً بترتيب أو زيارات أو اقتباسات من الذكاء الاصطناعي في أي نص أو توثيق تولّده.
10. **Guardrails.** Don't break the current design; don't change core app logic unless required; ship changes incrementally and safely; use the framework's own best practices; when several solutions exist, pick the **least risky and most compatible** one.
   - **ضوابط إلزامية.** لا تكسر التصميم الحالي؛ لا تغيّر منطق التطبيق الأساسي إلا عند الحاجة؛ طبّق التعديلات تدريجياً وبأمان؛ اتبع أفضل ممارسات إطار العمل؛ وعند تعدد الحلول اختر **الأقل خطورة والأكثر توافقاً**.
11. **Final report format:** (1) files changed, (2) improvements applied, (3) what was not applied and why, (4) test steps, (5) future recommendations — plus owner inputs and production-only checks from step 8.
   - **صيغة التقرير النهائي:** (1) الملفات المعدّلة، (2) التحسينات المطبّقة، (3) ما لم يُطبَّق ولماذا، (4) خطوات الاختبار، (5) توصيات مستقبلية — مع مدخلات المالك وفحوص الإنتاج من الخطوة 8.

---

## 1. Crawlability & robots.txt · قابلية الزحف وملف robots.txt

- [ ] [C] `/robots.txt` exists at the root, returns **200** (never 5xx or 429 — Google then treats the whole site as disallowed, and after ~30 days falls back to the last cached copy; other 4xx = no restrictions).
  - [C] الملف `/robots.txt` موجود في الجذر ويعيد **200** (لا يعيد 5xx أو 429 أبداً — تعتبر Google الموقع كله محظوراً حينها، وبعد نحو 30 يوماً تعود لآخر نسخة مخزّنة؛ بقية أكواد 4xx = بلا قيود).
- [ ] Does not block CSS, JS, images or important pages.
  - لا يحظر ملفات CSS أو JS أو الصور أو الصفحات المهمة.
- [ ] Declares `Sitemap: https://<host>/sitemap.xml` (absolute HTTPS; multiple lines allowed). The declared URL must resolve and validate.
  - يعلن `Sitemap: https://<host>/sitemap.xml` (رابط HTTPS مطلق؛ يُسمح بعدة أسطر). الرابط المعلن يجب أن يعمل ويكون صالحاً.
- [ ] Private paths (`/account`, `/checkout`, admin, dashboards) are protected by **auth**, not robots.txt — user-triggered agents may ignore robots.txt. [H]
  - المسارات الخاصة (`/account`، `/checkout`، لوحة الإدارة، لوحات التحكم) محمية **بتسجيل الدخول** وليس بـ robots.txt — الوكلاء الذين يطلقهم المستخدم قد يتجاهلون robots.txt. [H]
- [ ] RFC 9309: a crawler obeys only the most specific group that names it; the `*` group is ignored for it. Repeat directives (incl. `Content-Signal`) in every named group. [H]
  - وفق RFC 9309: الزاحف يلتزم فقط بالمجموعة الأكثر تحديداً التي تسمّيه، ويتجاهل مجموعة `*`. كرّر التوجيهات (بما فيها `Content-Signal`) في كل مجموعة مسمّاة. [H]
- [ ] Don't block crawlers by IP (a blocked crawler cannot read robots.txt).
  - لا تحظر الزواحف عبر IP (الزاحف المحظور لا يستطيع قراءة robots.txt).
- [ ] Important pages ≤ 3 clicks from the homepage; no orphan pages.
  - الصفحات المهمة على بُعد ≤ 3 نقرات من الرئيسية؛ لا صفحات يتيمة.
- [ ] Large sites (>10k pages): remove index bloat (faceted/filter/search/thin pages → noindex or consolidate).
  - المواقع الكبيرة (>10 آلاف صفحة): أزل تضخم الفهرس (صفحات الفلاتر/البحث/الصفحات الضعيفة ← noindex أو دمج).
- [ ] Keep critical content and JSON-LD within the first **2 MB** of uncompressed HTML (Googlebot fetch limit). Avoid inline base64 images, huge inline CSS/JS, bloated nav.
  - أبقِ المحتوى المهم وJSON-LD ضمن أول **2 ميجابايت** من HTML غير المضغوط (حد جلب Googlebot). تجنّب الصور المضمّنة بـ base64، وCSS/JS المضمّن الضخم، والقوائم المتضخمة.
- [ ] No AMP work (no ranking advantage; AMP isn't required for Top Stories). Don't add AMP cache/viewer or SXG.
  - لا عمل على AMP (لا ميزة ترتيب؛ وAMP ليس شرطاً لأهم الأخبار). لا تضف AMP cache/viewer أو SXG.
- [ ] IndexNow implemented for Bing/Yandex/Naver (not Google): submit changed URLs on publish/update. [L]
  - تطبيق IndexNow لـ Bing/Yandex/Naver (وليس Google): أرسل الروابط المتغيرة عند النشر/التحديث. [L]

### 1.1 AI crawler policy · سياسة زواحف الذكاء الاصطناعي

Decide per token. **Ask the owner for the AI-training policy; do not default-block.**

قرّر لكل زاحف على حدة. **اسأل المالك عن سياسة التدريب؛ لا تحظر افتراضياً.**

| User-agent |Owner<br>المالك|Purpose<br>الغرض|Notes<br>ملاحظات|
|---|---|---|---|
| Googlebot | Google |Search + AI Overviews<br>البحث + AI Overviews|Never block<br>لا تحظره أبداً|
| OAI-SearchBot | OpenAI |ChatGPT Search citations<br>الاقتباس في ChatGPT Search|Allow for AI-search visibility [H]<br>اسمح به للظهور في البحث بالذكاء الاصطناعي [H]|
| ChatGPT-User | OpenAI |User-triggered browsing<br>تصفح يطلقه المستخدم|robots may not apply<br>قد لا يلتزم بـ robots|
| GPTBot | OpenAI |Training only<br>تدريب فقط|Does not affect ChatGPT Search<br>لا يؤثر على ChatGPT Search|
| Claude-SearchBot | Anthropic |Claude search citations<br>الاقتباس في بحث Claude|Allow [H]<br>اسمح به [H]|
| Claude-User | Anthropic |User-triggered<br>يطلقه المستخدم|Honors robots<br>يلتزم بـ robots|
| ClaudeBot | Anthropic |Training only<br>تدريب فقط|Honors Crawl-delay<br>يلتزم بـ Crawl-delay|
| PerplexityBot | Perplexity |Search index<br>فهرس البحث|Allow [H]<br>اسمح به [H]|
| Perplexity-User | Perplexity |User-triggered<br>يطلقه المستخدم|Generally ignores robots<br>غالباً يتجاهل robots|
| Google-Extended | Google |Gemini model training + grounding in Gemini Apps / Vertex AI<br>تدريب نماذج Gemini والتأسيس في تطبيقات Gemini / Vertex AI|**No effect on Google Search inclusion or ranking** (AI Overviews draw on the Search index)<br>**لا أثر له على الظهور أو الترتيب في بحث Google** (تعتمد AI Overviews على فهرس البحث)|
| Applebot-Extended | Apple |Apple Intelligence training opt-out<br>الانسحاب من تدريب Apple Intelligence|Siri/Spotlight use Applebot<br>Siri/Spotlight تستخدم Applebot|
| CCBot | Common Crawl |Dataset/training<br>مجموعة بيانات/تدريب| — |
| Bytespider | ByteDance |Training<br>تدريب| — |
| cohere-ai / cohere-training-data-crawler | Cohere |Training<br>تدريب|Reported in third-party crawler lists; not officially documented<br>تذكرها قوائم زواحف خارجية؛ غير موثّقة رسمياً|
| Google-Agent, Google-GeminiNotebook (formerly Google-NotebookLM), GoogleMessages | Google |User-triggered<br>يطلقها المستخدم|Ignore robots — use server-side controls<br>تتجاهل robots — استخدم ضوابط على الخادم|

`Content-Signal` (Cloudflare, experimental; stated preference, no confirmed effect): `search=yes|no, ai-input=yes|no, ai-train=yes|no`. Place it inside **every** relevant group; never change Allow/Disallow when adding it.

`Content-Signal` (من Cloudflare، تجريبي؛ تفضيل معلن بلا أثر مؤكد): `search=yes|no, ai-input=yes|no, ai-train=yes|no`. ضعه داخل **كل** مجموعة معنية؛ ولا تغيّر Allow/Disallow عند إضافته.

Example (allow search & agents, deny training — use only if the owner chooses `ai-train=no`):

مثال (السماح بالبحث والوكلاء، ومنع التدريب — استخدمه فقط إن اختار المالك `ai-train=no`):

```
User-agent: *
Content-Signal: search=yes, ai-input=yes, ai-train=no
Allow: /

User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
Content-Signal: search=yes, ai-input=yes, ai-train=no
Allow: /

User-agent: GPTBot
User-agent: ClaudeBot
User-agent: Google-Extended
User-agent: CCBot
User-agent: Bytespider
Content-Signal: search=yes, ai-input=yes, ai-train=no
Disallow: /

Sitemap: https://example.com/sitemap.xml
```

(Remember to repeat private-path `Disallow` lines in every named group.)

(تذكّر تكرار أسطر `Disallow` للمسارات الخاصة في كل مجموعة مسمّاة.)

---

## 2. Indexability, canonicals, redirects · قابلية الفهرسة، الروابط القانونية (canonical)، التحويلات

- [ ] Every indexable page has a `<link rel="canonical">` — absolute, self-referencing (or intentionally pointing to the preferred URL). Never canonical + `noindex` together.
  - كل صفحة قابلة للفهرسة فيها `<link rel="canonical">` — رابط مطلق يشير إلى الصفحة نفسها (أو يشير عمداً إلى الرابط المفضّل). لا تجمع أبداً بين canonical و`noindex`.
- [ ] One host: pick www or non-www and HTTPS; 301 everything else to it.
  - نطاق واحد: اختر www أو بدونها مع HTTPS، وحوّل كل ما عداه بـ 301.
- [ ] Parameter/sort/filter URLs canonicalize to the base URL when duplicate or low-value.
  - روابط المعاملات/الفرز/الفلاتر تشير canonical إلى الرابط الأساسي إذا كانت مكررة أو منخفضة القيمة.
- [ ] Pagination: real crawlable `<a href>` links to each page; each paginated page self-canonicalizes (not to page 1). `rel=next/prev` is unused by Google. Infinite scroll / "load more" must be backed by real paginated URLs.
  - الترقيم: روابط `<a href>` حقيقية قابلة للزحف لكل صفحة؛ كل صفحة مرقّمة تشير canonical إلى نفسها (وليس إلى الصفحة 1). Google لا يستخدم `rel=next/prev`. التمرير اللانهائي / "تحميل المزيد" يجب أن تدعمه روابط ترقيم حقيقية.
- [ ] Meta robots `index, follow` unless intentionally blocked; no accidental `noindex` (staging flags, env checks).
  - Meta robots بقيمة `index, follow` إلا إذا كان الحظر مقصوداً؛ لا `noindex` عرضي (أعلام بيئة التجربة، فحوص البيئة).
- [ ] Redirects: 301 for permanent moves; **max 1 hop** (no chains, no loops). Legacy URLs that still have backlinks get 301s to the best match.
  - التحويلات: 301 للنقل الدائم؛ **قفزة واحدة كحد أقصى** (لا سلاسل ولا حلقات). الروابط القديمة التي لها روابط خلفية تُحوَّل بـ 301 إلى أنسب صفحة.
- [ ] Real 404 status for unknown URLs (no soft-404 / catch-all 200). Custom 404 page with navigation. Note: Google may skip rendering for non-200 responses, so don't rely on JS on error pages.
  - حالة 404 حقيقية للروابط غير الموجودة (لا soft-404 ولا 200 شاملة). صفحة 404 مخصصة فيها تنقّل. ملاحظة: قد لا يشغّل Google ملفات JS على الاستجابات غير 200، فلا تعتمد على JS في صفحات الخطأ.
- [ ] Trailing-slash behavior is consistent and identical in canonical, hreflang, sitemap and internal links.
  - سلوك الشرطة المائلة في نهاية الرابط ثابت ومتطابق في canonical وhreflang وخريطة الموقع والروابط الداخلية.

## 3. Rendering (SSR) requirements · متطلبات العرض من الخادم (SSR)

- [ ] [C] Primary content, title, meta description, canonical, meta robots, hreflang and JSON-LD are in the **initial server-rendered HTML**. Many AI crawlers are reported not to execute JavaScript (e.g. GPTBot, ClaudeBot, PerplexityBot, per third-party log analyses).
  - [C] المحتوى الأساسي، والعنوان، والوصف، وcanonical، وmeta robots، وhreflang، وJSON-LD موجودة في **HTML الأولي المولّد من الخادم**. تشير تحليلات خارجية إلى أن كثيراً من زواحف الذكاء الاصطناعي (مثل GPTBot وClaudeBot وPerplexityBot) لا تشغّل JS.
- [ ] Raw-HTML canonical == any JS-set canonical. Never rely on JS to remove a raw `noindex`.
  - canonical في HTML الخام == أي canonical يضبطه JS. لا تعتمد على JS لإزالة `noindex` موجود في HTML الخام.
- [ ] Time-sensitive markup (Product/Offer price & availability) is server-rendered, not JS-injected. [H]
  - البيانات الحساسة للوقت (سعر وتوفر Product/Offer) تُولّد من الخادم، لا تُحقن بـ JS. [H]
- [ ] Rendering strategy: SSR/SSG for public content; CSR only behind login. Dynamic rendering for bots is tech debt.
  - استراتيجية العرض: SSR/SSG للمحتوى العام؛ CSR فقط خلف تسجيل الدخول. العرض الديناميكي للزواحف دَين تقني.
- [ ] Verify with `curl -s <url>` / View Source that the key text, title, meta and JSON-LD exist without JavaScript — if not, it is the top priority. [C]
  - تحقّق عبر `curl -s <url>` أو "عرض المصدر" أن النص المهم والعنوان والوصف وJSON-LD موجودة دون JavaScript — وإن لم تكن، فهذه أولوية قصوى. [C]
- [ ] Per framework: **React SPA** → move key pages to SSR/SSG (prerender as a minimum); **Next.js/Nuxt** → key pages server-rendered or statically generated, not client-only; **Laravel/Blade** → already server-rendered, just ensure important parts aren't injected by JS after load.
  - حسب إطار العمل: **React SPA** ← تحويل الصفحات المهمة إلى SSR/SSG (أو Prerender كحد أدنى)؛ **Next.js/Nuxt** ← الصفحات المهمة Server Rendered أو Static Generated وليست Client-only؛ **Laravel/Blade** ← المحتوى أصلاً من الخادم، فقط تأكد أن الأجزاء المهمة ليست محقونة بـ JS بعد التحميل.

## 4. HTTPS & security · HTTPS والأمان

- [ ] [C] HTTPS everywhere, valid certificate, HTTP→HTTPS 301, no mixed content.
  - [C] HTTPS في كل مكان، شهادة صالحة، تحويل HTTP←HTTPS بـ 301، بلا محتوى مختلط.
- [ ] Headers: `Strict-Transport-Security`, `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, `X-Frame-Options` (or CSP `frame-ancestors`), `Referrer-Policy`.
  - الترويسات: `Strict-Transport-Security`، `Content-Security-Policy`، `X-Content-Type-Options: nosniff`، `X-Frame-Options` (أو `frame-ancestors` في CSP)، `Referrer-Policy`.
- [ ] Remove version disclosure (`X-Powered-By`, server version). Keep the runtime (e.g. PHP) on a patched release. [H]
  - أزل كشف الإصدارات (`X-Powered-By`، إصدار الخادم). أبقِ بيئة التشغيل (مثل PHP) على إصدار مُرقّع. [H]
- [ ] [C] **No back-button hijacking**: no `history.pushState/replaceState` tricks that trap the Back button — including from third-party ad/library scripts. Spam policy ("malicious practices"), announced 2026-04-13, enforced since 2026-06-15. Audit third-party scripts.
  - [C] **لا اختطاف لزر الرجوع**: لا حيل `history.pushState/replaceState` تحبس زر الرجوع — بما في ذلك من سكربتات إعلانات/مكتبات طرف ثالث. سياسة مكافحة سبام مطبّقة منذ 2026-06-15. دقّق سكربتات الطرف الثالث.

## 5. URL structure · بنية الروابط

- [ ] Lowercase, hyphenated, descriptive slugs; no query params for content; logical folder hierarchy reflecting site architecture.
  - روابط بأحرف صغيرة، بشرطات، وصفية؛ بلا معاملات استعلام للمحتوى؛ تسلسل مجلدات منطقي يعكس بنية الموقع.
- [ ] < 100 characters; no keyword stuffing; slugs unique (enforce at generation time).
  - أقل من 100 حرف؛ بلا حشو كلمات مفتاحية؛ الروابط فريدة (فرض ذلك عند التوليد).
- [ ] Non-Latin (e.g. Arabic) slugs: choose one strategy (transliterated Latin or UTF-8) consistently and percent-encode correctly in canonical/sitemap/hreflang.
  - الروابط غير اللاتينية (مثل العربية): اختر استراتيجية واحدة (نقل صوتي لاتيني أو UTF-8) بشكل ثابت، مع ترميز النسبة المئوية الصحيح في canonical/خريطة الموقع/hreflang.

## 6. Mobile & page experience · الجوال وتجربة الصفحة

- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1">`; responsive; no horizontal scroll at 375px.
  - `<meta name="viewport" content="width=device-width, initial-scale=1">`؛ تصميم متجاوب؛ لا تمرير أفقي على عرض 375px.
- [ ] Touch targets ≥ 24×24 CSS px (WCAG 2.2 AA); 44–48px recommended. Base font ≥ 16px.
  - أهداف اللمس ≥ 24×24 بكسل CSS (WCAG 2.2 AA)؛ يُوصى بـ 44–48px. حجم الخط الأساسي ≥ 16px.
- [ ] Mobile/desktop parity of content, headings, meta, structured data and links (mobile-first indexing).
  - تطابق المحتوى والعناوين والوسوم والبيانات المنظمة والروابط بين الجوال وسطح المكتب (الفهرسة تبدأ بالجوال).
- [ ] No intrusive interstitials, consent-redirect pages, or excessive ads. Primary content not hidden behind interaction; no scroll hijacking; preserve hash deep links.
  - لا نوافذ منبثقة مزعجة، ولا صفحات موافقة تحويلية، ولا إعلانات مفرطة. المحتوى الأساسي غير مخفي خلف تفاعل؛ لا اختطاف للتمرير؛ حافظ على روابط المرساة (#).
- [ ] Above the fold: H1 + primary CTA visible without scrolling; no layout shift. Check at 375×812, 768×1024, 1366×768, 1920×1080.
  - أعلى الصفحة: H1 + زر الإجراء الأساسي ظاهران بلا تمرير؛ بلا إزاحة في التخطيط. افحص على 375×812، 768×1024، 1366×768، 1920×1080.

## 7. Core Web Vitals & performance · مؤشرات أداء الويب الأساسية (Core Web Vitals) والأداء

Thresholds at p75 of real-user (CrUX) data. **INP replaced FID (never mention FID).**

الحدود عند المئين 75 من بيانات المستخدمين الحقيقيين (CrUX). **INP حلّ محل FID (لا تذكر FID أبداً).**

|Metric<br>المقياس|Good<br>جيد|Needs improvement<br>يحتاج تحسيناً|Poor<br>ضعيف|
|---|---|---|---|
| LCP |≤ 2.5 s<br>≤ 2.5 ث|2.5–4.0 s<br>2.5–4.0 ث|> 4.0 s<br>> 4.0 ث|
| INP |≤ 200 ms<br>≤ 200 مللي ث|200–500 ms<br>200–500 مللي ث|> 500 ms<br>> 500 مللي ث|
| CLS | ≤ 0.1 | 0.1–0.25 | > 0.25 |

TTFB target < 800 ms. Fix order: LCP → CLS → INP.

هدف TTFB أقل من 800 مللي ث. ترتيب الإصلاح: LCP ← CLS ← INP.

**LCP**

- [ ] LCP/hero image: preload, `fetchpriority="high"`, explicit width/height, **never** `loading="lazy"`, WebP/AVIF, compressed.
  - صورة LCP/الواجهة: preload، و`fetchpriority="high"`، وأبعاد صريحة، و**ممنوع** `loading="lazy"`، وصيغة WebP/AVIF، ومضغوطة.
- [ ] Inline critical CSS; defer non-critical CSS; `defer`/`async` scripts; defer third-party (analytics, chat).
  - CSS الحرج مضمّن؛ تأجيل CSS غير الحرج؛ `defer`/`async` للسكربتات؛ تأجيل سكربتات الطرف الثالث (التحليلات، الدردشة).
- [ ] Fonts: `font-display: swap` + preload the key font; self-host or `preconnect`.
  - الخطوط: `font-display: swap` + preload للخط الرئيسي؛ استضافة ذاتية أو `preconnect`.
- [ ] Cut TTFB: caching (page/route/query caches), CDN, compression (Brotli/gzip), HTTP/2+.
  - خفض TTFB: التخزين المؤقت (للصفحات/المسارات/الاستعلامات)، CDN، الضغط (Brotli/gzip)، HTTP/2 أو أحدث.

**INP**

- [ ] Break long tasks (< 50 ms chunks); debounce handlers; `requestAnimationFrame` for visual updates.
  - قسّم المهام الطويلة (أجزاء < 50 مللي ث)؛ استخدم debounce للمعالجات؛ `requestAnimationFrame` للتحديثات المرئية.
- [ ] DOM < ~1,400 elements (Lighthouse warning threshold); avoid layout thrashing, sync XHR, heavy localStorage work; limit main-thread third-party scripts.
  - عدد عناصر DOM أقل من ~1,400 (حد التحذير في Lighthouse)؛ تجنّب تكرار إعادة حساب التخطيط، وXHR المتزامن، والعمل الثقيل على localStorage؛ قلّل سكربتات الطرف الثالث على الخيط الرئيسي.

**CLS**

- [ ] width/height (or `aspect-ratio`) on all images, iframes, videos, embeds; reserve space for ads/banners; never inject content above existing content.
  - width/height (أو `aspect-ratio`) لكل الصور وiframes والفيديو والتضمينات؛ احجز مساحة للإعلانات/الشرائط؛ لا تُدرج محتوى فوق محتوى موجود.
- [ ] Long-lived cache headers for hashed static assets; consider Speculation Rules / bfcache-friendly pages (no `unload` handlers, no `Cache-Control: no-store` on public pages).
  - ترويسات تخزين مؤقت طويلة للملفات الثابتة ذات البصمة؛ فكّر في Speculation Rules وصفحات متوافقة مع bfcache (بلا معالجات `unload`، وبلا `Cache-Control: no-store` على الصفحات العامة).

## 8. On-page essentials (every indexable page) · أساسيات الصفحة (لكل صفحة قابلة للفهرسة)

- [ ] **Title**: one, unique, 30–60 chars (aim 50–60). Primary keyword near the start, brand at the end (` | Brand`). Not generic ("Home"). For Arabic see §20.2.
  - **العنوان (title)**: واحد، فريد، 30–60 حرفاً (الهدف 50–60). الكلمة المفتاحية الأساسية قرب البداية، والعلامة في النهاية (` | العلامة`). ليس عاماً ("الرئيسية"). للعربية راجع §20.2.
- [ ] **Meta description**: unique, 120–160 chars. Active voice, page-specific value + CTA. Must not repeat the title, must not end with the same stock CTA site-wide, no brand suffix, avoid double quotes. Templated metadata across many URLs is a **[H]** finding.
  - **الوصف (meta description)**: فريد، 120–160 حرفاً. بصيغة المبني للمعلوم، قيمة خاصة بالصفحة + دعوة لإجراء. لا يكرر العنوان، ولا ينتهي بنفس الدعوة الجاهزة في كل الموقع، ولا يُلحق به اسم العلامة، وتجنّب علامات الاقتباس المزدوجة. الأوصاف القالبية المتكررة عبر روابط كثيرة مشكلة **[H]**.
- [ ] **H1**: exactly one, matches intent, contains primary keyword. H2–H6 logical, no skipped levels, descriptive.
  - **H1**: واحد بالضبط، يطابق نية البحث، ويحوي الكلمة المفتاحية الأساسية. H2–H6 منطقية، بلا تخطي مستويات، ووصفية.
- [ ] Primary keyword in title, H1, slug, meta description and first 100 words — naturally. No keyword density target; no stuffing.
  - الكلمة المفتاحية الأساسية في العنوان وH1 والرابط والوصف وأول 100 كلمة — بشكل طبيعي. لا نسبة كثافة مستهدفة؛ لا حشو.
- [ ] **Open Graph**: `og:title`, `og:description`, `og:image` (absolute, ≥1200×630), `og:url`, `og:type`, `og:locale` (+ `og:locale:alternate`), `og:site_name`. **Twitter**: `twitter:card=summary_large_image`, `twitter:title`, `twitter:description`, `twitter:image`.
  - **Open Graph**: `og:title`، `og:description`، `og:image` (مطلق، ≥1200×630)، `og:url`، `og:type`، `og:locale` (+ `og:locale:alternate`)، `og:site_name`. **Twitter**: `twitter:card=summary_large_image`، `twitter:title`، `twitter:description`، `twitter:image`.
- [ ] `<html lang>` (and `dir="rtl"` for RTL locales) correct per page.
  - `<html lang>` (و`dir="rtl"` للغات RTL) صحيحة لكل صفحة.
- [ ] Favicon / apple-touch-icon / web manifest present.
  - Favicon / apple-touch-icon / web manifest موجودة.
- [ ] Internal links: descriptive, varied anchors (no "click here", no single anchor > 40% of links to a page); links inside body copy, not only nav. Targets: 3–5 per 1,000 words; blog 1,500+ words → 5–10; service page 3–5; product 2–4; category → all children.
  - الروابط الداخلية: نصوص وصفية متنوعة (لا "اضغط هنا"، ولا نص واحد يتجاوز 40% من الروابط لصفحة ما)؛ الروابط داخل متن المحتوى وليس في القوائم فقط. الأهداف: 3–5 لكل 1,000 كلمة؛ مقالة 1,500+ كلمة ← 5–10؛ صفحة خدمة 3–5؛ منتج 2–4؛ تصنيف ← كل الأبناء.
- [ ] Every page has ≥ 1 incoming internal link (blog/cluster posts ≥ 3).
  - لكل صفحة رابط داخلي وارد واحد على الأقل (مقالات المدونة/المجموعات ≥ 3).
- [ ] Breadcrumb navigation + `BreadcrumbList` schema on every non-home page.
  - مسار تنقّل (breadcrumb) + مخطط `BreadcrumbList` في كل صفحة غير الرئيسية.
- [ ] Semantic HTML: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`; important text visible in HTML, not hidden or JS-only.
  - HTML دلالي: `<header>` و`<nav>` و`<main>` و`<section>` و`<article>` و`<aside>` و`<footer>`؛ والنصوص المهمة ظاهرة داخل HTML وليست مخفية أو مولّدة من JS فقط.
- [ ] Share buttons on every shareable page (WhatsApp, X, LinkedIn, Facebook, Telegram, email, copy link, plus the native Web Share API on mobile) as plain `<a href>` share URLs with accessible labels — no heavy third-party SDKs (performance/privacy); complete OG/Twitter tags make the previews correct.
  - أزرار مشاركة في كل صفحة قابلة للمشاركة (واتساب، X، لينكدإن، فيسبوك، تيليجرام، البريد، نسخ الرابط، وWeb Share API على الجوال) كروابط `<a href>` عادية بأسماء وصول واضحة — دون مكتبات طرف ثالث ثقيلة (للأداء والخصوصية)؛ ووسوم OG/Twitter الكاملة تضمن ظهور المعاينة بشكل صحيح.
- [ ] External links to authoritative sources where claims are made.
  - روابط خارجية لمصادر موثوقة حيث توجد ادعاءات.
- [ ] Visible published date and "last updated" date on articles (real dates only — never fake freshness).
  - تاريخ نشر وتاريخ "آخر تحديث" ظاهران في المقالات (تواريخ حقيقية فقط — لا حداثة مزيفة أبداً).

## 9. XML sitemaps · خرائط الموقع XML

- [ ] [C] Valid XML, served over HTTPS, generated dynamically from real indexable URLs, referenced in robots.txt.
  - [C] XML صالح، يُقدَّم عبر HTTPS، يُولَّد ديناميكياً من الروابط الحقيقية القابلة للفهرسة، ومُشار إليه في robots.txt.
- [ ] [C] ≤ 50,000 URLs and ≤ 50 MB uncompressed per file; above that use a `<sitemapindex>`, split by type (pages, posts, products, images…).
  - [C] ≤ 50,000 رابط و≤ 50 ميجابايت غير مضغوط لكل ملف؛ فوق ذلك استخدم `<sitemapindex>` مقسّماً حسب النوع (صفحات، مقالات، منتجات، صور…).
- [ ] Only canonical, indexable, 200-status, HTTPS URLs. No noindexed [H], redirected [M] or 404 URLs.
  - فقط روابط canonical قابلة للفهرسة، بحالة 200، وHTTPS. لا روابط noindex [H]، ولا محوّلة [M]، ولا 404.
- [ ] `<lastmod>` = real last significant content change (W3C datetime), not generation time; not identical across all URLs. `<priority>`/`<changefreq>` are ignored — omit.
  - `<lastmod>` = تاريخ آخر تغيير جوهري حقيقي في المحتوى (صيغة W3C)، وليس وقت التوليد؛ وليس متطابقاً لكل الروابط. وسما `<priority>`/`<changefreq>` يتم تجاهلهما — احذفهما.
- [ ] Image sitemap: only `<image:image>`/`<image:loc>` (≤ 1,000 per URL); remove deprecated caption/title/geo/license tags.
  - خريطة الصور: فقط `<image:image>`/`<image:loc>` (≤ 1,000 لكل رابط)؛ أزل وسوم caption/title/geo/license الملغاة.
- [ ] Video sitemap (if videos): `thumbnail_loc`, `title`, `description`, `content_loc` or `player_loc`.
  - خريطة الفيديو (إن وُجد فيديو): `thumbnail_loc`، `title`، `description`، `content_loc` أو `player_loc`.
- [ ] News sitemap (publishers only): ≤ 1,000 items, last 2 days only.
  - خريطة الأخبار (للناشرين فقط): ≤ 1,000 عنصر، آخر يومين فقط.
- [ ] For multilingual sites, hreflang may live here via `xmlns:xhtml` (see §10) — use one method (HTML or sitemap); combining them is allowed but brings no benefit and makes conflicts more likely.
  - للمواقع متعددة اللغات، يمكن وضع hreflang هنا عبر `xmlns:xhtml` (راجع §10) — استخدم طريقة واحدة (HTML أو خريطة الموقع)؛ الجمع بينهما مسموح لكنه بلا فائدة ويزيد احتمال التعارض.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://example.com/page</loc><lastmod>2026-02-07</lastmod></url>
</urlset>
```

## 10. Hreflang / international (conditional: multi-language or multi-region) · Hreflang / التدويل (مشروط: تعدد اللغات أو المناطق)

- [ ] [C] Every page in an alternate set includes a **self-referencing** hreflang whose URL equals its canonical exactly.
  - [C] كل صفحة في مجموعة البدائل تتضمن hreflang **يشير إلى نفسها**، ورابطه مطابق تماماً لـ canonical الخاص بها.
- [ ] [C] **Reciprocal** (full mesh): if A → B then B → A, across all alternates.
  - [C] **تبادلية** (شبكة كاملة): إذا أشار A إلى B فيجب أن يشير B إلى A، عبر كل البدائل.
- [ ] [M] Exactly one `x-default` per set (language selector or primary-language fallback).
  - [M] `x-default` واحد بالضبط لكل مجموعة (صفحة اختيار اللغة أو اللغة الأساسية الاحتياطية).
- [ ] [H] Codes: ISO 639-1 language (`ar`, `en`), optional ISO 3166-1 region in `ar-SA` form. Invalid: `en-uk`, `jp`, `eng`, region without language.
  - [H] الرموز: لغة ISO 639-1 (`ar`، `en`)، مع منطقة ISO 3166-1 اختيارية بصيغة `ar-SA`. غير صالح: `en-uk`، `jp`، `eng`، منطقة بلا لغة.
- [ ] [H] Hreflang only on canonical URLs; same protocol/host/trailing slash as canonicals.
  - [H] hreflang فقط على روابط canonical؛ بنفس البروتوكول/النطاق/الشرطة النهائية لروابط canonical.
- [ ] Methods: `<link rel="alternate" hreflang="…" href="…">` in `<head>`, HTTP `Link` header (non-HTML files such as PDFs), or sitemap `xhtml:link` (easier for large sites). Prefer one method; combining gives no benefit.
  - الطرق: `<link rel="alternate" hreflang="…" href="…">` في `<head>`، أو ترويسة HTTP `Link` (للملفات غير HTML مثل PDF)، أو `xhtml:link` في خريطة الموقع (أسهل للمواقع الكبيرة). فضّل طريقة واحدة؛ الجمع بلا فائدة.
- [ ] Each locale: translated title/meta/H1/schema/OG, correct `lang`/`dir`, locale-correct number/date/currency/phone formats (international phone with country code). Content parity across languages.
  - لكل لغة: عنوان/وصف/H1/مخطط/OG مترجمة، `lang`/`dir` صحيحان، صيغ أرقام/تواريخ/عملات/هواتف صحيحة محلياً (الهاتف بالصيغة الدولية مع رمز الدولة). تكافؤ المحتوى بين اللغات.
- [ ] Mass, unreviewed machine translation that adds no value can be treated as scaled content abuse. Human-review translations.
  - الترجمة الآلية الجماعية غير المراجَعة التي لا تضيف قيمة قد تُعامل كإساءة محتوى واسع النطاق. يجب مراجعة الترجمات بشرياً.
- [ ] Don't auto-redirect by IP/Accept-Language without a visible way to switch; crawlers must reach every locale URL.
  - لا تحويل تلقائي حسب IP/Accept-Language دون وسيلة ظاهرة للتبديل؛ يجب أن تصل الزواحف إلى كل رابط لغة.

```html
<link rel="alternate" hreflang="ar" href="https://example.com/ar/page">
<link rel="alternate" hreflang="en" href="https://example.com/en/page">
<link rel="alternate" hreflang="x-default" href="https://example.com/ar/page">
```

## 11. Images · الصور

- [ ] Every `<img>` has `alt`: 10–125 chars describing the subject; decorative → `alt=""`. No filenames, no "image of", no stuffing.
  - كل `<img>` له `alt`: 10–125 حرفاً يصف موضوع الصورة؛ الصور الزخرفية ← `alt=""`. لا أسماء ملفات، ولا "صورة لـ"، ولا حشو.
- [ ] `width` + `height` (or `aspect-ratio`) on every image.
  - `width` + `height` (أو `aspect-ratio`) لكل صورة.
- [ ] `loading="lazy"` only below the fold; `decoding="async"` on non-LCP images; LCP image `fetchpriority="high"`.
  - `loading="lazy"` فقط أسفل الطيّة؛ `decoding="async"` للصور غير LCP؛ صورة LCP بـ `fetchpriority="high"`.
- [ ] Responsive `srcset` (e.g. 400w/800w/1200w) + `sizes`.
  - `srcset` متجاوب (مثلاً 400w/800w/1200w) + `sizes`.
- [ ] Formats: AVIF/WebP with JPEG fallback via `<picture>`; PNG for transparency; SVG for icons/logos. Don't ship JPEG XL.
  - الصيغ: AVIF/WebP مع بديل JPEG عبر `<picture>`؛ PNG للشفافية؛ SVG للأيقونات والشعارات. لا تستخدم JPEG XL.
- [ ] Size budgets: thumbnails < 50 KB (crit > 200 KB), content < 100 KB (crit > 500 KB), hero < 200 KB (crit > 700 KB).
  - ميزانيات الحجم: المصغّرات < 50KB (حرج > 200KB)، صور المحتوى < 100KB (حرج > 500KB)، صور الواجهة < 200KB (حرج > 700KB).
- [ ] Descriptive lowercase hyphenated filenames (`blue-running-shoes.webp`, not `IMG_1234.jpg`). Long cache headers / CDN.
  - أسماء ملفات وصفية بأحرف صغيرة وشرطات (`blue-running-shoes.webp` وليس `IMG_1234.jpg`). ترويسات تخزين مؤقت طويلة / CDN.
- [ ] AI-generated product images must carry IPTC `DigitalSourceType` = `trainedAlgorithmicMedia` (`compositeWithTrainedAlgorithmicMedia` for AI-edited images); don't strip this metadata (Merchant Center requirement).
  - صور المنتجات المولّدة بالذكاء الاصطناعي يجب أن تحمل IPTC `DigitalSourceType` = `trainedAlgorithmicMedia` (و`compositeWithTrainedAlgorithmicMedia` للصور المعدّلة بالذكاء الاصطناعي)؛ ولا تحذف هذه البيانات (مطلب Merchant Center).

```html
<picture>
  <source srcset="hero.avif" type="image/avif">
  <source srcset="hero.webp" type="image/webp">
  <img src="hero.jpg" alt="Descriptive alt" width="1200" height="630" fetchpriority="high">
</picture>
```

*مثال عربي · Arabic example:*

```html
<picture>
  <source srcset="hero.avif" type="image/avif">
  <source srcset="hero.webp" type="image/webp">
  <img src="hero.jpg" alt="نص بديل وصفي" width="1200" height="630" fetchpriority="high">
</picture>
```

## 12. Structured data (JSON-LD) · البيانات المنظمة (JSON-LD)

### 12.1 Rules · القواعد

- [ ] [H] JSON-LD only (`<script type="application/ld+json">`), server-rendered.
  - [H] JSON-LD فقط (`<script type="application/ld+json">`)، مولّد من الخادم.
- [ ] [C] Valid JSON; `"@context": "https://schema.org"`; every node has `@type`; prefer one `@graph` per page with stable `@id`s (`https://example.com/#org`, `#website`, `<url>#webpage`).
  - [C] JSON صالح؛ `"@context": "https://schema.org"`؛ لكل عقدة `@type`؛ فضّل `@graph` واحداً لكل صفحة بمعرّفات `@id` ثابتة (`https://example.com/#org`، `#website`، `<url>#webpage`).
- [ ] [C] No placeholders; data matches visible content; ratings/reviews only from real, visible reviews (no fake or undisclosed incentivized reviews).
  - [C] بلا نصوص مؤقتة؛ البيانات مطابقة للمحتوى الظاهر؛ التقييمات/المراجعات من مراجعات حقيقية ظاهرة فقط (لا مراجعات مزيفة أو مدفوعة غير مُفصح عنها).
- [ ] [H] Absolute URLs; ISO 8601 dates; correct types (e.g. `price` as a number or numeric string with a `.` decimal and no currency symbol).
  - [H] روابط مطلقة؛ تواريخ ISO 8601؛ أنواع بيانات صحيحة (مثل `price` رقماً أو نصاً رقمياً بفاصلة عشرية `.` ودون رمز العملة).
- [ ] Validate with Rich Results Test + validator.schema.org; add an automated test that parses every page's JSON-LD.
  - تحقق عبر Rich Results Test وvalidator.schema.org؛ أضف اختباراً آلياً يحلل JSON-LD في كل صفحة.
- [ ] Don't claim schema improves AI citations.
  - لا تدّعِ أن المخطط يحسّن الاقتباس في الذكاء الاصطناعي.

### 12.2 Retired rich-result types (don't add for SERP benefit) · أنواع أُوقفت نتائجها المنسّقة (لا تضفها لفائدة في النتائج)

`HowTo` (rich results removed Sept 2023); `SpecialAnnouncement`, `CourseInfo`, `EstimatedSalary`, `LearningVideo`, `ClaimReview`, `VehicleListing` (phased out of Search, announced June 2025); Practice Problem (announced Nov 2025, removed Jan 2026); `Attorney` (deprecated in schema.org — use `LegalService` + `Person`). These no longer produce Google rich results; don't add them for SERP benefit. Exception: fact-checkers may keep `ClaimReview`, which Fact Check Explorer still uses.

`HowTo` (أُزيلت نتائجه المنسّقة سبتمبر 2023)؛ `SpecialAnnouncement` و`CourseInfo` و`EstimatedSalary` و`LearningVideo` و`ClaimReview` و`VehicleListing` (أُلغيت من البحث، أُعلن ذلك يونيو 2025)؛ Practice Problem (أُعلن نوفمبر 2025 وأُزيل يناير 2026)؛ `Attorney` (ملغى في schema.org — استخدم `LegalService` + `Person`). هذه الأنواع لم تعد تُنتج نتائج منسّقة في Google؛ لا تضفها لفائدة في نتائج البحث. استثناء: يمكن لمواقع تدقيق الحقائق إبقاء `ClaimReview` لأن Fact Check Explorer ما زال يستخدمه.

**FAQPage**: Google FAQ rich results stopped appearing on 2026-05-07 (Google still parses the markup). Don't add it for SERP benefit; existing markup may stay [I]. Use `QAPage` only for genuine user Q&A. Keep FAQ *content* on the page (it is still useful).

**FAQPage**: توقفت النتائج المنسّقة للأسئلة الشائعة في Google منذ 2026-05-07 (وما زالت Google تقرأ الترميز). لا تضفه لفائدة في نتائج البحث؛ الموجود منه يمكن إبقاؤه [I]. استخدم `QAPage` فقط لأسئلة وأجوبة حقيقية من المستخدمين. أبقِ *محتوى* الأسئلة الشائعة في الصفحة (ما زال مفيداً).

### 12.3 Per page type · حسب نوع الصفحة

|Page<br>الصفحة|Types<br>الأنواع|Key properties<br>الخصائص الأساسية|
|---|---|---|
|Site-wide (home)<br>على مستوى الموقع (الرئيسية)|`Organization` (or LocalBusiness subtype) + `WebSite`<br>`Organization` (أو نوع فرعي من LocalBusiness) + `WebSite`|name, url, logo, contactPoint, sameAs[]; WebSite name, url, inLanguage<br>name، url، logo، contactPoint، sameAs[]؛ ولـ WebSite: name، url، inLanguage|
|Every page<br>كل صفحة| `WebPage` + `BreadcrumbList` |name, description, inLanguage, isPartOf #website; itemListElement(position, name, item)<br>name، description، inLanguage، isPartOf #website؛ itemListElement(position، name، item)|
|Article/blog<br>مقالة/مدونة| `Article`/`BlogPosting`/`NewsArticle` |headline, author(Person + url), datePublished, dateModified, image, publisher #org; spokes add `isPartOf` pillar<br>headline، author(Person + url)، datePublished، dateModified، image، publisher #org؛ المقالات الفرعية تضيف `isPartOf` للصفحة المحورية|
|Author page<br>صفحة كاتب|`ProfilePage` → `Person`<br>`ProfilePage` ← `Person`|name, jobTitle, url, image, sameAs, worksFor, description<br>name، jobTitle، url، image، sameAs، worksFor، description|
|SaaS / tool<br>SaaS / أداة| `SoftwareApplication` / `WebApplication` |name, applicationCategory, operatingSystem, offers, aggregateRating (real), featureList<br>name، applicationCategory، operatingSystem، offers، aggregateRating (حقيقي)، featureList|
|Service<br>خدمة| `Service` / `ProfessionalService` |name, provider #org, areaServed, description, offers<br>name، provider #org، areaServed، description، offers|
|Product<br>منتج|`Product` (+ `ProductGroup` for variants)<br>`Product` (+ `ProductGroup` للمتغيرات)|see §16<br>راجع §16|
|Local<br>محلي|specific `LocalBusiness` subtype<br>نوع فرعي محدد من `LocalBusiness`|see §15<br>راجع §15|
|Hub / pillar / list<br>محور / قائمة| `ItemList` |itemListElement(position, url, name), numberOfItems<br>itemListElement(position، url، name)، numberOfItems|
|Comparison<br>مقارنة|`ItemList` (+ Product/SoftwareApplication with real ratings)<br>`ItemList` (+ Product/SoftwareApplication بتقييمات حقيقية)| — |
|Video<br>فيديو| `VideoObject` |name, description, thumbnailUrl, uploadDate, duration, contentUrl/embedUrl, creator; `Clip`/`SeekToAction` for key moments<br>name، description، thumbnailUrl، uploadDate، duration، contentUrl/embedUrl، creator؛ `Clip`/`SeekToAction` للحظات المهمة|
|Event<br>فعالية| `Event` |name, startDate, endDate, location, organizer, offers (rich result only for public, physical-location events)<br>name، startDate، endDate، location، organizer، offers (النتيجة المنسّقة فقط للفعاليات العامة في مكان فعلي)|
|Jobs<br>وظائف| `JobPosting` |title, description, datePosted, hiringOrganization, jobLocation, baseSalary<br>title، description، datePosted، hiringOrganization، jobLocation، baseSalary|
|Contact / About<br>تواصل / من نحن| `ContactPage` / `AboutPage` |name, url<br>name، url|

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "Organization", "@id": "https://example.com/#org", "name": "", "url": "https://example.com/",
     "logo": "https://example.com/logo.png", "sameAs": [],
     "contactPoint": {"@type": "ContactPoint", "telephone": "", "contactType": "customer service"}},
    {"@type": "WebSite", "@id": "https://example.com/#website", "url": "https://example.com/", "name": "",
     "publisher": {"@id": "https://example.com/#org"}, "inLanguage": "ar"},
    {"@type": "WebPage", "@id": "https://example.com/page#webpage", "url": "https://example.com/page", "name": "",
     "isPartOf": {"@id": "https://example.com/#website"}, "inLanguage": "ar"},
    {"@type": "BreadcrumbList", "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com/"},
      {"@type": "ListItem", "position": 2, "name": "Page", "item": "https://example.com/page"}]}
  ]
}
```

*مثال عربي · Arabic example:*

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "Organization", "@id": "https://example.com/#org", "name": "", "url": "https://example.com/",
     "logo": "https://example.com/logo.png", "sameAs": [],
     "contactPoint": {"@type": "ContactPoint", "telephone": "", "contactType": "customer service"}},
    {"@type": "WebSite", "@id": "https://example.com/#website", "url": "https://example.com/", "name": "",
     "publisher": {"@id": "https://example.com/#org"}, "inLanguage": "ar"},
    {"@type": "WebPage", "@id": "https://example.com/page#webpage", "url": "https://example.com/page", "name": "",
     "isPartOf": {"@id": "https://example.com/#website"}, "inLanguage": "ar"},
    {"@type": "BreadcrumbList", "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "الرئيسية", "item": "https://example.com/"},
      {"@type": "ListItem", "position": 2, "name": "الصفحة", "item": "https://example.com/page"}]}
  ]
}
```

(Empty strings above are slots to fill with real data — never ship them empty.)

(النصوص الفارغة أعلاه خانات تُملأ ببيانات حقيقية — لا تنشرها فارغة أبداً.)

- [ ] `WebSite` → `potentialAction: SearchAction` **only** when a real on-site search URL exists; never point it at a nonexistent search. (Google retired the sitelinks search box in Nov 2024; this markup no longer has a Google SERP effect.) [H]
  - أضف `SearchAction` داخل `WebSite` **فقط** عند وجود بحث داخلي حقيقي؛ ولا توجّهه أبداً إلى بحث غير موجود. (أوقفت Google مربع البحث في روابط الموقع في نوفمبر 2024؛ ولم يعد لهذا الترميز أثر في نتائج Google.) [H]

## 13. Content quality & E-E-A-T · جودة المحتوى وE-E-A-T (الخبرة، التخصص، الموثوقية، الجدارة بالثقة)

### 13.1 Trust pages & signals (site-wide) · صفحات وإشارات الثقة (على مستوى الموقع)

- [ ] About page (who, why, team), Contact page (address, phone, email, form), Privacy policy, Terms. Linked in footer.
  - صفحة من نحن (من، ولماذا، الفريق)، صفحة تواصل (العنوان، الهاتف، البريد، نموذج)، سياسة الخصوصية، الشروط والأحكام. مرتبطة في التذييل.
- [ ] Knowledge pages that help search engines and LLMs understand the site: About, Services/Products overview, **one detail page per service/product**, FAQ, Privacy, Terms (create any that are missing, with real content).
  - صفحات معرفية تساعد المحركات والنماذج على فهم الموقع: من نحن، نظرة عامة على الخدمات/المنتجات، **صفحة تفصيلية لكل خدمة/منتج**، الأسئلة الشائعة، الخصوصية، الشروط (أنشئ الناقص منها بمحتوى حقيقي).
- [ ] Author system: byline with name + credentials on every article, linked author bio page (`ProfilePage`/`Person`, photo, credentials, sameAs). Strongly recommended for YMYL (health, finance, legal, news, civic).
  - نظام الكتّاب: اسم الكاتب ومؤهلاته على كل مقالة، مع رابط لصفحة سيرته (`ProfilePage`/`Person`، صورة، مؤهلات، sameAs). ضروري بشدة لمواضيع YMYL (الصحة، المال، القانون، الأخبار، الشأن المدني).
- [ ] Visible published + "last updated" dates; flag fast-changing content > 12 months old.
  - تاريخ نشر و"آخر تحديث" ظاهران؛ نبّه على المحتوى سريع التغيّر الذي مضى عليه أكثر من 12 شهراً.
- [ ] Reviews/testimonials (real), certifications, awards, "as featured in" (real only), case studies with numbers.
  - مراجعات/شهادات (حقيقية)، شهادات اعتماد، جوائز، "كما ظهر في" (حقيقي فقط)، دراسات حالة بأرقام.
- [ ] Editorial/correction policy; disclosure of AI-assisted process where readers would ask; affiliate disclosures.
  - سياسة تحرير/تصحيح؛ الإفصاح عن استخدام الذكاء الاصطناعي حيث يتساءل القارئ؛ إفصاحات التسويق بالعمولة.
- [ ] No deceptive patterns (hidden ads, clickbait).
  - لا أساليب خادعة (إعلانات مخفية، عناوين مضللة).

### 13.2 Minimum content per page type (coverage floors, not targets) · الحد الأدنى للمحتوى حسب نوع الصفحة (حدود تغطية، وليست أهدافاً)

|Page type<br>نوع الصفحة|Min words<br>أدنى عدد كلمات|Unique<br>نسبة التفرّد|
|---|---|---|
|Homepage<br>الرئيسية| 500 | 100% |
|Service / feature<br>خدمة / ميزة| 800 | 100% |
|Landing<br>صفحة هبوط| 600 | 100% |
|Blog post<br>مقالة مدونة| 1,500 | 100% |
|Pillar<br>صفحة محورية (Pillar)| 2,500–4,000 | 100% |
|Cluster spoke<br>مقالة فرعية في مجموعة| 1,200–1,800 | 100% |
|Comparison<br>مقارنة| 1,500 | 100% |
|Product<br>منتج| 300–400 |80%+ (not manufacturer copy)<br>80%+ (ليس نص المصنّع)|
|Category<br>تصنيف|400 (unique intro)<br>400 (مقدمة فريدة)| 100% |
|About<br>من نحن| 400 | 100% |
|Location (primary / secondary)<br>موقع جغرافي (أساسي / ثانوي)| 600 / 500 | 60%+ / 40%+ |
|Glossary entry<br>مدخل في المسرد|200+ with examples<br>200+ مع أمثلة| 100% |

< 100 retrievable words = thin (or JS-gated). Readability heuristic: Flesch 60–70, sentences 15–20 words, paragraphs 2–4 sentences. Flesch applies to English only; for Arabic use sentence/paragraph length; word floors are approximate across languages.

أقل من 100 كلمة قابلة للاستخراج = محتوى ضعيف (أو محجوب بـ JS). مؤشر سهولة القراءة إرشادي: Flesch 60–70، الجمل 15–20 كلمة، الفقرات 2–4 جمل. مقياس Flesch خاص بالإنجليزية؛ للعربية اعتمد على طول الجملة والفقرة؛ وحدود عدد الكلمات تقريبية بين اللغات.

### 13.3 Structure & citability (SEO fundamentals that also help AI answers) · البنية وقابلية الاقتباس (أساسيات SEO تفيد أيضاً إجابات الذكاء الاصطناعي)

- [ ] Answer-first: direct answer/definition in the first 40–60 words of each section ("X is…").
  - الإجابة أولاً: إجابة/تعريف مباشر في أول 40–60 كلمة من كل قسم ("X هو…").
- [ ] Question-style H2/H3 from real "People Also Ask" questions; tables for comparisons; lists for steps; TOC on long content; TL;DR on long posts.
  - عناوين H2/H3 بصيغة أسئلة مأخوذة من "أسئلة ذات صلة" الحقيقية؛ جداول للمقارنات؛ قوائم للخطوات؛ فهرس محتويات للمحتوى الطويل؛ ملخص (TL;DR) للمقالات الطويلة.
- [ ] Specific facts and statistics with named, linked sources; original data, case studies, expert quotes.
  - حقائق وإحصاءات محددة بمصادر مسمّاة ومرتبطة؛ بيانات أصلية، دراسات حالة، اقتباسات خبراء.
- [ ] Information gain: each page states what it adds that top-ranking pages don't.
  - القيمة المضافة: كل صفحة تحدد ما تضيفه ولا تقدمه الصفحات الأعلى ترتيباً.
- [ ] Media: ≥ 1 relevant original image per post (not stock where possible); video/charts where useful.
  - الوسائط: صورة أصلية واحدة على الأقل لكل مقالة (وليست صوراً جاهزة حيثما أمكن)؛ فيديو/رسوم بيانية حيث يفيد.

### 13.4 AI-generated content rules · قواعد المحتوى المولّد بالذكاء الاصطناعي

- [ ] Allowed only with human review, fact-check, original insight and author attribution.
  - مسموح فقط مع مراجعة بشرية، وتدقيق للحقائق، ورؤية أصلية، ونسبة إلى كاتب.
- [ ] Never mass-generate pages without added value (scaled content abuse — also covers spinning and auto-translation).
  - لا توليد جماعي لصفحات بلا قيمة مضافة (إساءة محتوى واسع النطاق — تشمل أيضاً إعادة الصياغة الآلية والترجمة الآلية).
- [ ] Clean drafts: strip stray zero-width/bidi/tag characters, but keep ZWJ/ZWNJ where the script needs them (emoji sequences, Persian/Urdu, Indic); replace AI-typical phrasing ("delve into" etc.).
  - نظّف المسودات: احذف المحارف صفرية العرض ومحارف الاتجاه ومحارف الوسوم الشاردة، مع إبقاء ZWJ/ZWNJ حيث يحتاجها النظام الكتابي (تسلسلات الرموز التعبيرية، الفارسية والأردية، الأنظمة الهندية)؛ واستبدل العبارات النمطية للذكاء الاصطناعي.
- [ ] Avoid site reputation abuse (third-party low-quality content on your domain) and expired-domain abuse.
  - تجنّب إساءة سمعة الموقع (استضافة محتوى طرف ثالث رديء على نطاقك) وإساءة النطاقات المنتهية.

## 14. Site architecture, topic clusters, page types · بنية الموقع، مجموعات المواضيع، أنواع الصفحات

### 14.1 Hub-and-spoke · المحور والفروع (Hub-and-spoke)

- [ ] Pillar (broad keyword, 2,500–4,000 words, TOC, a section per cluster) links to **every** spoke; `Article` + `ItemList` + `BreadcrumbList`.
  - الصفحة المحورية (كلمة مفتاحية واسعة، 2,500–4,000 كلمة، فهرس محتويات، قسم لكل مجموعة) ترتبط بـ **كل** المقالات الفرعية؛ مخطط `Article` + `ItemList` + `BreadcrumbList`.
- [ ] 2–5 clusters per pillar, 2–4 spokes per cluster. Each spoke links to the pillar in body copy, to 2–3 siblings, 0–1 cross-cluster links; reachable from pillar in ≤ 2 clicks.
  - 2–5 مجموعات لكل صفحة محورية، و2–4 مقالات فرعية لكل مجموعة. كل مقالة فرعية ترتبط بالصفحة المحورية داخل المتن، وبـ 2–3 مقالات شقيقة، و0–1 رابط لمجموعة أخرى؛ ويمكن الوصول إليها من المحورية بنقرتين على الأكثر.
- [ ] No cannibalization: one primary keyword per URL; merge or differentiate near-duplicates.
  - لا تنافس داخلي: كلمة مفتاحية أساسية واحدة لكل رابط؛ ادمج أو ميّز الصفحات شبه المكررة.

### 14.2 Page-type ↔ intent match (SXO) · مطابقة نوع الصفحة لنية البحث (SXO)

Each URL is exactly one type; its type must match what the SERP rewards for its keyword.

كل رابط من نوع واحد بالضبط؛ ويجب أن يطابق النوع ما تكافئه نتائج البحث لكلمته المفتاحية.

|Type<br>النوع|Must have<br>يجب أن يحتوي|
|---|---|
|Landing<br>صفحة هبوط|CTA above fold, trust badges, ≥ 1 testimonial, 3 feature blocks, "how it works", pricing, FAQ, repeated CTA<br>دعوة لإجراء أعلى الصفحة، شارات ثقة، شهادة واحدة على الأقل، 3 كتل مزايا، "كيف يعمل"، الأسعار، أسئلة شائعة، دعوة متكررة|
|Blog post<br>مقالة مدونة|Article schema, author + dates, TOC, TL;DR, body meeting the §13.2 floor, image w/ alt, related posts<br>مخطط Article، الكاتب + التواريخ، فهرس محتويات، ملخص، متن يحقق الحد الأدنى في §13.2، صورة بنص بديل، مقالات ذات صلة|
|Product<br>منتج|Product schema, price + CTA above fold, gallery (4–6), rating/reviews, specs table, related products<br>مخطط Product، السعر + زر الشراء أعلى الصفحة، معرض (4–6)، تقييم/مراجعات، جدول مواصفات، منتجات ذات صلة|
|Service<br>خدمة|Service schema, problem → 3–5 step process, case studies w/ metrics, credentials, pricing hint, contact form<br>مخطط Service، المشكلة ← عملية من 3–5 خطوات، دراسات حالة بأرقام، المؤهلات، مؤشر للسعر، نموذج تواصل|
|Comparison<br>مقارنة|criteria, matrix table, pros/cons, "best for", verdict, ItemList schema<br>المعايير، جدول مقارنة، الإيجابيات/السلبيات، "الأفضل لـ"، الحكم النهائي، مخطط ItemList|
|Local<br>محلي|LocalBusiness subtype, full NAP, map, hours, geo<br>نوع فرعي من LocalBusiness، الاسم والعنوان والهاتف كاملة، خريطة، ساعات العمل، الإحداثيات|
|Tool<br>أداة|working tool above fold, no login wall, how-to (≤ 3 steps), WebApplication schema<br>أداة تعمل أعلى الصفحة، بلا اشتراط تسجيل دخول، طريقة الاستخدام (≤ 3 خطوات)، مخطط WebApplication|
|Hybrid<br>هجين|educational + commercial CTAs, clear value proposition<br>دعوات تعليمية وتجارية معاً، قيمة مقترحة واضحة|

Critical mismatches to fix: a blog post targeting a product, service, tool or "[service] in [city]" keyword; a landing page targeting a how-to keyword.

حالات عدم التطابق الحرجة التي يجب إصلاحها: مقالة مدونة تستهدف كلمة مفتاحية لمنتج أو خدمة أو أداة أو "[خدمة] في [مدينة]"؛ صفحة هبوط تستهدف كلمة مفتاحية من نوع "كيف".

### 14.3 Programmatic pages (conditional) · الصفحات المولّدة برمجياً (مشروط)

- [ ] Each page passes the standalone-value test; no "mad-libs" (only a name swapped). Conditional sections render only when data exists.
  - كل صفحة تجتاز اختبار القيمة المستقلة؛ لا قوالب "املأ الفراغ" (يتغير فيها الاسم فقط). الأقسام الشرطية تظهر فقط عند توفر البيانات.
- [ ] Gates: < 40% unique → thin; < 30% → stop. < 300 words → review. Shared boilerplate > 60% → avoid. 100+ unreviewed pages → content audit; 500+ → explicit approval.
  - الحدود: تفرّد < 40% ← ضعيف؛ < 30% ← توقف. < 300 كلمة ← مراجعة. نص قالب مشترك > 60% ← تجنّب. 100+ صفحة غير مراجعة ← تدقيق محتوى؛ 500+ ← موافقة صريحة.
- [ ] Location pages: WARNING at 30+, HARD STOP at 50+ without justification (real presence, unique local content).
  - صفحات المواقع الجغرافية: تحذير عند 30+، و**توقف** عند 50+ دون مبرر (وجود حقيقي، محتوى محلي فريد).
- [ ] Self-canonical; hubs link to all generated pages; each page links to 3–5 related by shared attributes; noindex thin records; human-review 5–10% sample; roll out in batches of 50–100.
  - canonical ذاتي؛ صفحات المحور ترتبط بكل الصفحات المولّدة؛ كل صفحة ترتبط بـ 3–5 صفحات ذات صلة حسب السمات المشتركة؛ noindex للسجلات الضعيفة؛ مراجعة بشرية لعيّنة 5–10%؛ النشر على دفعات من 50–100.

### 14.4 Comparison / "alternatives" pages (conditional) · صفحات المقارنة / "البدائل" (مشروط)

- [ ] Verifiable, sourced competitor claims; "as of [date]" on pricing; "Not publicly available" instead of guesses; honest strengths; disclose that the product is yours; methodology section; "Last updated"; quarterly review.
  - ادعاءات عن المنافسين قابلة للتحقق ومصدرها مذكور؛ "حتى تاريخ [..]" على الأسعار؛ "غير متاح علناً" بدل التخمين؛ ذكر نقاط قوة المنافس بأمانة؛ الإفصاح أن المنتج منتجك؛ قسم للمنهجية؛ "آخر تحديث"؛ مراجعة كل ثلاثة أشهر.
- [ ] No aggressive CTAs inside competitor sections. H1 < 70 chars.
  - لا دعوات عدوانية لإجراء داخل أقسام المنافسين. H1 أقل من 70 حرفاً.

## 15. Local SEO (conditional: physical location or service area) · السيو المحلي (مشروط: موقع فعلي أو منطقة خدمة)

- [ ] NAP (name, address, phone) identical in visible HTML (footer/contact), JSON-LD and Google Business Profile. Phone as `tel:` link.
  - الاسم والعنوان والهاتف (NAP) متطابقة في HTML الظاهر (التذييل/التواصل)، وJSON-LD، وملف Google التجاري. الهاتف كرابط `tel:`.
- [ ] Title/H1 include service + city on local pages. Hours visible. Embedded map (lazy-loaded) + directions link (brick-and-mortar only).
  - العنوان/H1 يتضمنان الخدمة + المدينة في الصفحات المحلية. ساعات العمل ظاهرة. خريطة مضمّنة (بتحميل كسول) + رابط الاتجاهات (للمواقع الفعلية فقط).
- [ ] One dedicated page per core service; one crawlable server-rendered URL per location at `/locations/<city>/`; store locator links to them.
  - صفحة مخصصة لكل خدمة أساسية؛ رابط واحد قابل للزحف ومولّد من الخادم لكل موقع في `/locations/<city>/`؛ وأداة البحث عن الفروع ترتبط بها.
- [ ] Location pages: primary > 60% unique, secondary > 40% (§13.2), below 30% = stop (local photos, staff, area testimonials, local FAQ). Swap test: if swapping the city name still reads fine, it's a doorway page.
  - صفحات المواقع: الأساسية تفرّد > 60%، والثانوية > 40% (§13.2)، وأقل من 30% = توقف (صور محلية، فريق، شهادات من المنطقة، أسئلة محلية). اختبار الاستبدال: إن كان استبدال اسم المدينة لا يغيّر شيئاً، فهي صفحة مدخل (doorway).
- [ ] Specific `LocalBusiness` subtype (Dentist, Plumber, Restaurant, LegalService…), not generic. Properties: `name` (= GBP), `address` (PostalAddress), `geo` (≥ 5 decimals), `telephone`, `url`, `openingHoursSpecification`, `priceRange` (< 100 chars), `image`. Don't add `aggregateRating`/`review` about your own business on your own site (self-serving → ineligible for stars); show third-party reviews visibly instead. Service-area businesses: `areaServed`, no `streetAddress`.
  - نوع فرعي محدد من `LocalBusiness` (Dentist، Plumber، Restaurant، LegalService…)، وليس عاماً. الخصائص: `name` (= Google التجاري)، `address` (PostalAddress)، `geo` (≥ 5 منازل عشرية)، `telephone`، `url`، `openingHoursSpecification`، `priceRange` (< 100 حرف)، `image`. ولا تضف `aggregateRating`/`review` عن نشاطك التجاري في موقعك (مراجعات ذاتية ← غير مؤهلة للنجوم)؛ واعرض مراجعات الأطراف الخارجية بشكل ظاهر بدلاً من ذلك. الأعمال ذات منطقة الخدمة: `areaServed` بلا `streetAddress`.
- [ ] Multi-location: Organization `@id` on home; each location its own `@id` + `parentOrganization` (pointing to the Organization `@id`).
  - تعدد الفروع: `@id` للمنظمة في الرئيسية؛ ولكل فرع `@id` خاص + `parentOrganization` (يشير إلى `@id` المنظمة).
- [ ] Reviews: show count and rating; no review gating. FAQs live on the site (Google Business Profile Q&A has been retired — its API ended Nov 2025 — and is being replaced by AI answers).
  - المراجعات: اعرض العدد والتقييم؛ لا انتقاء للمراجعات. الأسئلة الشائعة على موقعك (أُوقفت ميزة الأسئلة والأجوبة في ملف Google التجاري — انتهت واجهتها البرمجية في نوفمبر 2025 — وتُستبدل بإجابات الذكاء الاصطناعي).

## 16. E-commerce (conditional) · التجارة الإلكترونية (مشروط)

- [ ] [C] `Product`: `name`, `image[]` (crawlable, ideally ≥ 50K pixels width × height; 16:9, 4:3 or 1:1), `offers` (merchant listings: `Offer` — the page must be the seller; `AggregateOffer` only for product snippets on review/comparison pages).
  - [C] `Product`: `name`، `image[]` (قابلة للزحف، ويُفضّل ≥ 50 ألف بكسل للعرض × الارتفاع؛ بنسب 16:9 أو 4:3 أو 1:1)، `offers` (قوائم التاجر: `Offer` — الصفحة هي البائع؛ و`AggregateOffer` فقط لمقتطفات المنتجات في صفحات المراجعات والمقارنات).
- [ ] [C] `price` > 0 as a number or numeric string without currency symbol; `priceCurrency` ISO 4217; `availability` full URL (`https://schema.org/InStock`).
  - [C] `price` > 0 رقماً أو نصاً رقمياً بلا رمز عملة؛ `priceCurrency` بصيغة ISO 4217؛ `availability` رابط كامل (`https://schema.org/InStock`).
- [ ] [H] Recommended: `hasMerchantReturnPolicy` (`MerchantReturnPolicy` with `applicableCountry` + `returnPolicyCategory`; `merchantReturnDays` when the window is finite), or define it once at `Organization` level; plus `shippingDetails` (`OfferShippingDetails` with `shippingRate`, `shippingDestination`, `deliveryTime`).
  - [H] موصى به: `hasMerchantReturnPolicy` (`MerchantReturnPolicy` مع `applicableCountry` و`returnPolicyCategory`، و`merchantReturnDays` عند تحديد مدة للإرجاع)، أو تعريفها مرة واحدة على مستوى `Organization`؛ بالإضافة إلى `shippingDetails` (`OfferShippingDetails` مع `shippingRate` و`shippingDestination` و`deliveryTime`).
- [ ] Recommended: `sku`, `gtin`/`mpn`, `brand.name`, `description`, real `aggregateRating`/`review`, `color`/`size`/`material`, `category`, sale windows (`validFrom` + `priceValidUntil`).
  - موصى به: `sku`، `gtin`/`mpn`، `brand.name`، `description`، `aggregateRating`/`review` حقيقية، `color`/`size`/`material`، `category`، فترات التخفيض (`validFrom` + `priceValidUntil`).
- [ ] Variants: `ProductGroup` (`productGroupID`, `variesBy`, `hasVariant`); no duplicate H1 across variants.
  - المتغيرات: `ProductGroup` (`productGroupID`، `variesBy`، `hasVariant`)؛ لا تكرار لـ H1 بين المتغيرات.
- [ ] Product page: title `<Product> - <Feature> | <Brand>` < 60 chars; unique description meeting the §13.2 floor (not manufacturer copy); specs table; on-page reviews; breadcrumbs Home > Category > Sub > Product; ≥ 3 images.
  - صفحة المنتج: عنوان `<المنتج> - <الميزة> | <العلامة>` أقل من 60 حرفاً؛ وصف فريد يحقق الحد الأدنى في §13.2 (وليس نص المصنّع)؛ جدول مواصفات؛ مراجعات في الصفحة؛ مسار تنقّل الرئيسية > التصنيف > الفرعي > المنتج؛ ≥ 3 صور.
- [ ] Category pages: unique intro (≥ 400 words), crawlable pagination, faceted URLs canonicalized/noindexed.
  - صفحات التصنيف: مقدمة فريدة (≥ 400 كلمة)، ترقيم قابل للزحف، روابط الفلاتر بـ canonical/noindex.

## 17. Agent readiness (AI agents & Lighthouse "Agentic Browsing") · الجاهزية للوكلاء (وكلاء الذكاء الاصطناعي وفئة Lighthouse "Agentic Browsing")

**P0 · أولوية قصوى**

- [ ] Accessibility tree clean (the accessibility subset Lighthouse uses for Agentic Browsing passes — names/labels, tree integrity, visibility): accessible names on buttons/links/inputs/selects, valid ARIA roles/attributes, `document-title`, no `aria-hidden` on focusable elements, no duplicate ARIA ids, valid `tabindex`, `autocomplete` values valid, SVG images have names.
  - شجرة إمكانية الوصول نظيفة (اجتياز مجموعة قواعد إمكانية الوصول التي يعتمدها Lighthouse في Agentic Browsing — الأسماء والتسميات، وسلامة الشجرة، والظهور): أسماء وصول للأزرار/الروابط/الحقول/القوائم، أدوار وخصائص ARIA صالحة، `document-title`، لا `aria-hidden` على عناصر قابلة للتركيز، لا معرّفات ARIA مكررة، `tabindex` صالح، قيم `autocomplete` صالحة، صور SVG لها أسماء.
- [ ] Real elements: `<button>` for actions, `<a href>` for navigation, native inputs; no `<div onclick>`. Every input has a `<label>`/`aria-label`. Landmarks: `<header> <nav> <main> <article> <aside> <footer>`.
  - عناصر حقيقية: `<button>` للإجراءات، `<a href>` للتنقل، حقول إدخال أصلية؛ لا `<div onclick>`. لكل حقل `<label>`/`aria-label`. المعالم: `<header> <nav> <main> <article> <aside> <footer>`.
- [ ] CLS ≤ 0.1; primary content present without JS; no CAPTCHA/WAF challenge on content pages for verified bots.
  - CLS ≤ 0.1؛ المحتوى الأساسي موجود بلا JS؛ لا CAPTCHA أو تحدي WAF على صفحات المحتوى للزواحف الموثّقة.

**P1 · أولوية عالية**

- [ ] No hover-only menus, focus traps, toast-only confirmations, transparent overlays capturing clicks, infinite scroll without paginated links.
  - لا قوائم تظهر عند مرور المؤشر فقط، ولا مصائد تركيز، ولا تأكيدات عابرة فقط (toast)، ولا طبقات شفافة تلتقط النقرات، ولا تمرير لا نهائي بلا روابط ترقيم.
- [ ] Unknown URLs return real 404.
  - الروابط غير الموجودة تعيد 404 حقيقية.
- [ ] `/llms.txt` (optional; Google Search doesn't need or use it for ranking or AI features, but Lighthouse's experimental Agentic Browsing category checks for it; useful for docs/dev-facing sites; never pitch as a ranking lever):
  - `/llms.txt` (اختياري؛ بحث Google لا يحتاجه ولا يستخدمه للترتيب أو لميزات الذكاء الاصطناعي، لكن فئة Agentic Browsing التجريبية في Lighthouse تتحقق من وجوده؛ مفيد لمواقع التوثيق والمطورين؛ لا تقدّمه أبداً كوسيلة ترتيب):

```
# Site Name
> One-sentence description of the site.

## Main pages
- [Pricing](https://example.com/pricing): Plans and prices
- [Docs](https://example.com/docs): Getting started

## Optional
- [Changelog](https://example.com/changelog): Release history
```

*مثال عربي · Arabic example:*

```
# اسم الموقع
> وصف الموقع في جملة واحدة.

## الصفحات الرئيسية
- [الأسعار](https://example.com/pricing): الخطط والأسعار
- [التوثيق](https://example.com/docs): البدء

## Optional
- [سجل التغييرات](https://example.com/changelog): تاريخ الإصدارات
```

Rules: H1 required (llmstxt.org); a blockquote summary and H2 link lists recommended; Lighthouse's audit reportedly also expects ≥ 1 link and a minimum length. Generate from real routes. (`## Optional` stays in English: it is a keyword of the format.)

القواعد: H1 إلزامي (llmstxt.org)؛ ويُنصح بملخص في اقتباس وقوائم روابط تحت H2؛ وتشير تقارير إلى أن فحص Lighthouse يتوقع رابطاً واحداً على الأقل وحداً أدنى للطول. يُولَّد من المسارات الحقيقية. (عنوان `## Optional` يبقى بالإنجليزية لأنه كلمة محجوزة في الصيغة.)

- [ ] llms.txt contents: one-line site description, key pages, main products/services, docs/articles links, and short factual context on what the site covers (facts, not instructions to promote it — see §22.8).
  - محتوى llms.txt: وصف مختصر للموقع، أهم الصفحات، أهم المنتجات/الخدمات، روابط التوثيق/المقالات، وسياق مختصر يشرح ما يغطيه الموقع (حقائق، وليس تعليمات للترويج — راجع §22.8).

**P2–P3 (only if relevant) · (فقط إن كانت ذات صلة)**

- [ ] Markdown alternates (`/page.md` with `<link rel="alternate" type="text/markdown">`, or `Accept: text/markdown` negotiation with `Vary: Accept`) — content-equivalent, never cloaking.
  - نسخ Markdown بديلة (`/page.md` مع `<link rel="alternate" type="text/markdown">`، أو التفاوض عبر `Accept: text/markdown` مع `Vary: Accept`) — مكافئة في المحتوى، ولا إخفاء (cloaking) أبداً.
- [ ] `/.well-known/api-catalog` (RFC 9727, `application/linkset+json`), OAuth metadata (RFC 8414 / RFC 9728), `/.well-known/agent-card.json` (A2A), `/.well-known/ai-catalog.json` (early draft, very low adoption) — only if you actually run those services; otherwise real 404.
  - `/.well-known/api-catalog` (RFC 9727)، وبيانات OAuth الوصفية (RFC 8414 / RFC 9728)، و`/.well-known/agent-card.json` (A2A)، و`/.well-known/ai-catalog.json` (مسودة مبكرة قليلة الاعتماد) — فقط إن كنت تشغّل هذه الخدمات فعلاً؛ وإلا 404 حقيقية.
- [ ] WebMCP (`document.modelContext.registerTool`) for key read-only actions (e.g. site search); consequential actions need `consequentialHint: true` + human confirmation; same authz/validation as the UI. Experimental (origin trial; the API has changed — older drafts used `navigator.modelContext`): feature-detect, and mark read-only tools `readOnlyHint: true`. Optional; absence is not a defect.
  - WebMCP (`document.modelContext.registerTool`) للإجراءات المهمة للقراءة فقط (مثل البحث في الموقع)؛ الإجراءات المؤثرة تحتاج `consequentialHint: true` + تأكيداً بشرياً؛ بنفس الصلاحيات والتحقق الموجودين في الواجهة. تجريبي (Origin Trial؛ وتغيّرت الواجهة — المسودات القديمة استخدمت `navigator.modelContext`): تحقّق من دعم الميزة، وعلّم أدوات القراءة بـ `readOnlyHint: true`. اختياري؛ غيابه ليس عيباً.

## 18. Release regression checklist (SEO drift) · قائمة فحص التراجع عند الإصدار (انحراف السيو)

Capture a baseline of key templates before deploy; compare after. Fail the release on any CRITICAL. Automate as tests where possible.

التقط خط أساس للقوالب الرئيسية قبل النشر وقارن بعده. أفشل الإصدار عند أي بند حرج. حوّل البنود إلى اختبارات آلية حيثما أمكن.

|Severity<br>الخطورة|Rule<br>القاعدة|
|---|---|
|CRITICAL<br>حرج|JSON-LD removed · canonical changed or removed · `noindex` newly added · H1 removed or substantially changed · title removed/empty · status 2xx → 4xx/5xx<br>حذف JSON-LD · تغيير canonical أو حذفه · إضافة `noindex` جديدة · حذف H1 أو تغييره جوهرياً · حذف العنوان/فراغه · تغيّر الحالة من 2xx إلى 4xx/5xx|
|WARNING<br>تحذير|title or meta description changed · CWV p75 > 20% worse · Lighthouse perf −10 pts · OG tags removed · schema content changed<br>تغيّر العنوان أو الوصف · تراجع CWV عند المئين 75 بأكثر من 20% · انخفاض أداء Lighthouse 10 نقاط · حذف وسوم OG · تغيّر محتوى المخطط|
|INFO<br>معلومة|new JSON-LD (validate it) · H2 structure changed · HTML hash changed<br>JSON-LD جديد (تحقق منه) · تغيّر بنية H2 · تغيّر بصمة HTML|

## 19. Measurement (owner tasks — list them in the report) · القياس (مهام المالك — اذكرها في التقرير)

- [ ] Verify the site in Google Search Console and Bing Webmaster Tools; submit sitemaps; keep the Search Console generative-AI setting so the site stays included in AI Overviews/AI Mode (opting out removes those impressions and visits).
  - توثيق الموقع في Google Search Console وBing Webmaster Tools؛ إرسال خرائط الموقع؛ إبقاء إعداد الذكاء الاصطناعي التوليدي في Search Console على السماح بظهور الموقع في AI Overviews / AI Mode (إلغاؤه يحذف الظهور والزيارات منها).
- [ ] Analytics (GA4/Matomo/etc.) with organic segmentation; consent-compliant.
  - أداة تحليلات (GA4/Matomo/غيرها) مع تقسيم الزيارات العضوية؛ ومتوافقة مع متطلبات موافقة المستخدم (ملفات الارتباط).
- [ ] Monitor Core Web Vitals (field data), indexing coverage, and indexed-count vs intended-count monthly.
  - مراقبة Core Web Vitals (البيانات الميدانية)، وتغطية الفهرسة، وعدد الصفحات المفهرسة مقابل المستهدف شهرياً.
- [ ] Off-site (not code): Google Business Profile, citations, reviews, digital PR, brand presence (YouTube, LinkedIn, Wikipedia/Wikidata) with `sameAs` links.
  - خارج الموقع (ليس كوداً): ملف Google التجاري، الإدراج في الأدلة، المراجعات، العلاقات العامة الرقمية، الحضور (YouTube، LinkedIn، Wikipedia/Wikidata) مع روابط `sameAs`.

---

## 20. Arabic & RTL SEO (conditional: any Arabic, Hebrew, Persian, Urdu locale) · السيو للعربية واتجاه RTL (مشروط: أي لغة عربية أو عبرية أو فارسية أو أردية)

> Arabic is a primary language: these items apply to every Arabic page, and most apply to all RTL languages.

> العربية لغة أساسية: هذه البنود تُطبَّق على كل صفحة عربية، وأغلبها يسري على كل لغات RTL.

### 20.1 Document & markup · المستند والترميز

- [ ] [C] `<html lang="ar" dir="rtl">` on Arabic pages (`lang="ar-SA"` etc. only if the content is region-specific). Never `dir="rtl"` on an English page.
  - [C] `<html lang="ar" dir="rtl">` في الصفحات العربية (`lang="ar-SA"` ونحوها فقط إن كان المحتوى خاصاً بمنطقة). لا تضع `dir="rtl"` أبداً على صفحة إنجليزية.
- [ ] [H] `<meta charset="utf-8">` is the first element in `<head>`; responses send `Content-Type: text/html; charset=utf-8`.
  - [H] `<meta charset="utf-8">` أول عنصر في `<head>`؛ والاستجابات ترسل `Content-Type: text/html; charset=utf-8`.
- [ ] Layout uses CSS logical properties (`margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `text-align: start`) — no hardcoded left/right; icons with direction (arrows, chevrons, progress) are mirrored in RTL.
  - التخطيط يستخدم خصائص CSS المنطقية (`margin-inline-start`، `padding-inline-end`، `inset-inline-start`، `text-align: start`) — لا يمين/يسار ثابت؛ والأيقونات ذات الاتجاه (الأسهم، وعلامات الشيفرون، وأشرطة التقدم) معكوسة في RTL.
- [ ] Mixed-direction strings (English brand/product names, numbers, URLs, emails, phone numbers inside Arabic text) are wrapped in `<bdi>` or `dir="ltr"` spans so they don't scramble. Phone numbers and emails always `dir="ltr"`.
  - النصوص مختلطة الاتجاه (أسماء علامات/منتجات إنجليزية، أرقام، روابط، بريد، أرقام هواتف داخل نص عربي) داخل `<bdi>` أو `dir="ltr"` حتى لا تختلط. أرقام الهواتف والبريد دائماً `dir="ltr"`.
- [ ] No stray bidi control characters (U+200E/U+200F/U+202A–U+202E/U+2066–U+2069) or tatweel (ـ) inside `<title>`, meta description, slugs, JSON-LD or headings. Strip them server-side.
  - لا محارف تحكم اتجاه شاردة (U+200E/U+200F/U+202A–U+202E/U+2066–U+2069) ولا تطويل (ـ) داخل `<title>` أو الوصف أو الروابط أو JSON-LD أو العناوين. احذفها من جهة الخادم.
- [ ] Text normalized to Unicode NFC before storage and output.
  - تطبيع النص بصيغة Unicode NFC قبل الحفظ والعرض.

### 20.2 Metadata in Arabic · البيانات الوصفية بالعربية

- [ ] Title/description truncation is pixel-based and unpublished (~600px for titles is a common estimate); glyph widths differ by script and font. As a *heuristic* start from **≈ 45–55 chars** title and **≈ 110–140 chars** description for Arabic, and test the SERP preview rather than trusting the Latin character limits in §8.
  - قطع العنوان والوصف يعتمد على البكسل وحدوده غير منشورة (~600px للعنوان تقدير شائع)؛ وعرض الحروف يختلف حسب النظام الكتابي والخط. كبداية *إرشادية* للعربية استهدف **≈ 45–55 حرفاً** للعنوان و**≈ 110–140 حرفاً** للوصف، واختبر معاينة نتائج البحث بدل الاعتماد على حدود الأحرف اللاتينية في §8.
- [ ] Brand placement: `<عنوان الصفحة> | <العلامة>` — the separator and brand sit at the logical end (visual left).
  - موضع العلامة: `<عنوان الصفحة> | <العلامة>` — الفاصل والعلامة في النهاية المنطقية (يسار الشاشة).
- [ ] Use Arabic punctuation in Arabic copy: `،` `؛` `؟` and Arabic quotation marks `« »` (avoid ASCII `"` in descriptions).
  - استخدم علامات الترقيم العربية في النص العربي: `،` `؛` `؟` وعلامات التنصيص العربية `« »` (تجنّب `"` في الأوصاف).
- [ ] `og:locale="ar_AR"` (Facebook's pan-Arabic code; region codes like `ar_SA` are OGP-valid but may be ignored by Facebook) + `og:locale:alternate="en_US"`; OG/Twitter images with Arabic text designed RTL (Arabic text in the image, readable at small size).
  - `og:locale="ar_AR"` (رمز Facebook للعربية العامة؛ ورموز المناطق مثل `ar_SA` صالحة في OGP لكن قد يتجاهلها Facebook) + `og:locale:alternate="en_US"`؛ صور OG/Twitter التي فيها نص عربي مصممة من اليمين لليسار (النص مقروء حتى بحجم صغير).
- [ ] JSON-LD: `"inLanguage": "ar"` on WebSite/WebPage/Article; Arabic `name`/`headline`/`description`; `alternateName` holds the Latin/English brand name; `ContactPoint.availableLanguage: ["Arabic","English"]`.
  - JSON-LD: `"inLanguage": "ar"` في WebSite/WebPage/Article؛ `name`/`headline`/`description` بالعربية؛ `alternateName` يحمل الاسم اللاتيني/الإنجليزي للعلامة؛ `ContactPoint.availableLanguage: ["Arabic","English"]`.
- [ ] [H] Each metadata field (title, description, OG, schema `name`) is written in the page's language — never a full translation pair in one field; a Latin brand name or an established Latin term may appear (keep it short, avoid bidi issues); the brand in the other script goes to `alternateName`.
  - [H] كل حقل بيانات وصفية (العنوان، الوصف، OG، `name` في المخطط) يُكتب بلغة الصفحة — ولا تضع ترجمتين في حقل واحد؛ ويجوز ظهور اسم علامة لاتيني أو مصطلح لاتيني شائع (باختصار ومع تجنّب مشكلات اتجاه النص)؛ واسم العلامة بالنظام الكتابي الآخر يوضع في `alternateName`.

### 20.3 Arabic keyword & content strategy · استراتيجية الكلمات المفتاحية والمحتوى العربي

- [ ] Keyword research in Arabic, not translated from English. Cover **MSA + major dialect phrasings** people actually type (e.g. "كيف أسوي" / "كيف أعمل" / "ازاي أعمل"), plus Arabizi/Franco ("3arabi") and English loan terms ("AI" vs "الذكاء الاصطناعي") where the audience searches that way.
  - البحث عن الكلمات المفتاحية بالعربية مباشرة، وليس بترجمتها من الإنجليزية. غطِّ **الفصحى + صيغ اللهجات الرئيسية** التي يكتبها الناس فعلاً (مثل "كيف أسوي" / "كيف أعمل" / "ازاي أعمل")، بالإضافة إلى العربيزي ("3arabi") والمصطلحات الإنجليزية الدخيلة ("AI" مقابل "الذكاء الاصطناعي") حيث يبحث الجمهور بها.
- [ ] Spelling variants exist in queries: hamza forms (أ/إ/آ/ا), taa marbuta vs haa (ة/ه), alef maqsura vs yaa (ى/ي), with/without diacritics. Use the most-searched form in title/H1 and natural variants in body; never stuff all variants.
  - تتنوع الكتابة في الاستعلامات: أشكال الهمزة (أ/إ/آ/ا)، التاء المربوطة مقابل الهاء (ة/ه)، الألف المقصورة مقابل الياء (ى/ي)، مع/بدون تشكيل. استخدم الصيغة الأكثر بحثاً في العنوان/H1 والصيغ الأخرى طبيعياً في المتن؛ لا تحشُ كل الصيغ.
- [ ] Definite-article variants matter ("ذكاء اصطناعي" vs "الذكاء الاصطناعي"); include both naturally.
  - صيغ أداة التعريف مهمة ("ذكاء اصطناعي" مقابل "الذكاء الاصطناعي")؛ أدرج كلتيهما بشكل طبيعي.
- [ ] Region targeting: `ar` for pan-Arab content; `ar-SA`, `ar-AE`, `ar-EG`… only when content (currency, laws, dialect, prices) truly differs, each with its own URL + hreflang.
  - الاستهداف الإقليمي: `ar` للمحتوى العربي العام؛ `ar-SA`، `ar-AE`، `ar-EG`… فقط عندما يختلف المحتوى فعلاً (العملة، القوانين، اللهجة، الأسعار)، ولكل منها رابط خاص + hreflang.
- [ ] [H] No unreviewed machine translation from English; Arabic pages are written or edited by a fluent Arabic editor (scaled-content-abuse risk + quality).
  - [H] لا ترجمة آلية غير مراجعة من الإنجليزية؛ الصفحات العربية يكتبها أو يحررها محرر يتقن العربية (خطر إساءة المحتوى واسع النطاق + الجودة).
- [ ] Arabic content parity: Arabic pages are not thinner than their English counterparts (same sections, FAQs, schema, internal links).
  - تكافؤ المحتوى العربي: الصفحات العربية ليست أضعف من نظيراتها الإنجليزية (نفس الأقسام، الأسئلة الشائعة، المخطط، الروابط الداخلية).

### 20.4 Numbers, dates, currency · الأرقام والتواريخ والعملات

- [ ] Pick **one** digit system per locale for visible text (Western `0-9` is safest for search; Eastern Arabic `٠-٩` if the brand requires it) and apply consistently. Machine-readable values (JSON-LD, `datetime`, `price`, `tel:`) always use Western digits.
  - اختر نظام أرقام **واحداً** لكل لغة في النص الظاهر (الأرقام اللاتينية `0-9` — وتُسمّى أيضاً العربية — الأكثر أماناً للبحث؛ أو المشرقية/الهندية `٠-٩` إن تطلبتها العلامة) وطبّقه بثبات. القيم المقروءة آلياً (JSON-LD، `datetime`، `price`، `tel:`) دائماً بالأرقام اللاتينية (0-9).
- [ ] Dates: `<time datetime="2026-11-05">5 نوفمبر 2026</time>` (`datetime` is always ISO 8601 Gregorian); Gregorian month names per region (يناير vs كانون الثاني); Hijri may be shown alongside in the visible text.
  - التواريخ: `<time datetime="2026-11-05">5 نوفمبر 2026</time>` (قيمة `datetime` دائماً ميلادية بصيغة ISO 8601)؛ أسماء الأشهر الميلادية حسب المنطقة (يناير مقابل كانون الثاني)؛ ويمكن عرض الهجري بجانبه في النص الظاهر.
- [ ] Currency with ISO code in schema (`SAR`, `AED`, `EGP`) and locale-correct visible formatting (`٤٩٫٠٠ ر.س` or `49.00 SAR`).
  - العملة برمز ISO في المخطط (`SAR`، `AED`، `EGP`) وبتنسيق ظاهر صحيح محلياً (`٤٩٫٠٠ ر.س` أو `49.00 SAR`).

### 20.5 URLs & on-site search for Arabic · الروابط والبحث الداخلي للعربية

- [ ] Slug strategy chosen once: **Arabic UTF-8 slugs** (readable in SERP, longer when percent-encoded) **or** transliterated Latin (short, shareable). Whatever is chosen: consistent across canonical, hreflang, sitemap and internal links; percent-encoded correctly; never both versions live without a 301.
  - اختر استراتيجية الروابط مرة واحدة: **روابط عربية UTF-8** (مقروءة في نتائج البحث، وأطول عند ترميزها) **أو** نقل صوتي لاتيني (قصيرة وسهلة المشاركة). أياً كان الاختيار: ثابت في canonical وhreflang وخريطة الموقع والروابط الداخلية؛ مُرمّز بشكل صحيح؛ ولا تُبقِ النسختين معاً دون تحويل 301.
- [ ] Translated slugs per locale where possible (`/en/pricing` ↔ `/ar/الأسعار` or `/ar/pricing`) — the alternate mapping comes from data, not string replacement.
  - روابط مترجمة لكل لغة حيث أمكن (`/en/pricing` ↔ `/ar/الأسعار` أو `/ar/pricing`) — ربط البدائل يأتي من البيانات، لا من استبدال النصوص.
- [ ] On-site search normalizes Arabic (strip diacritics + tatweel, unify أإآ→ا, ة→ه, ى→ي) on both index and query so users find content regardless of spelling.
  - البحث داخل الموقع يطبّع العربية (حذف التشكيل والتطويل، توحيد أإآ←ا، ة←ه، ى←ي) في الفهرس والاستعلام معاً حتى يجد المستخدم المحتوى مهما كانت طريقة كتابته.

### 20.6 Fonts & performance for Arabic · الخطوط والأداء للعربية

- [ ] Arabic web font subset to the Arabic + Latin ranges actually used (`unicode-range`), WOFF2, `font-display: swap`, preload the primary weight only.
  - خط ويب عربي مقلّص إلى نطاقات العربية واللاتينية المستخدمة فعلاً (`unicode-range`)، بصيغة WOFF2، مع `font-display: swap`، وpreload للوزن الأساسي فقط.
- [ ] Line-height ≥ 1.6 for Arabic body text; no letter-spacing on Arabic (breaks joined letters); no `text-transform`.
  - ارتفاع السطر ≥ 1.6 لنص المتن العربي؛ لا تباعد أحرف (letter-spacing) في العربية (يكسر اتصال الحروف)؛ لا `text-transform`.
- [ ] Fallback stack includes a system Arabic font with matched metrics (`size-adjust`, `ascent-override`) — or use `font-display: optional` — to limit invisible text and CLS on swap.
  - قائمة الخطوط الاحتياطية تتضمن خطاً عربياً من النظام بمقاييس مطابقة (`size-adjust` و`ascent-override`) — أو استخدم `font-display: optional` — للحد من النص غير المرئي وإزاحة التخطيط عند التبديل.

---

## 21. All languages & scripts (multilingual / international) · كل اللغات والأنظمة الكتابية (تعدد اللغات / التدويل)

Applies whenever the site has, or will have, more than one language. Extends §10.

ينطبق كلما كان للموقع، أو سيكون له، أكثر من لغة. يوسّع §10.

### 21.1 Architecture · البنية

- [ ] One URL per language version, preferably **subdirectories** (`/ar/`, `/en/`, `/fr/`); ccTLDs only for strong country targeting; avoid `?lang=` parameters and cookie-only language switching.
  - رابط واحد لكل نسخة لغة، ويُفضَّل **المجلدات الفرعية** (`/ar/`، `/en/`، `/fr/`)؛ نطاقات الدول (ccTLD) فقط لاستهداف قوي لدولة؛ تجنّب معاملات `?lang=` وتبديل اللغة بملفات الارتباط فقط.
- [ ] Language is decided by URL. Only the root `/` may auto-redirect (302, e.g. by Accept-Language), and it should be the `x-default`; locale URLs never auto-redirect by IP, cookie or Accept-Language; never block crawlers from reaching other locales.
  - اللغة يحددها الرابط. الجذر `/` وحده يمكن أن يحوّل تلقائياً (302، مثلاً حسب Accept-Language) ويكون هو `x-default`؛ وروابط اللغات لا تحوّل تلقائياً أبداً حسب IP أو ملفات الارتباط أو Accept-Language؛ ولا تمنع الزواحف من الوصول إلى اللغات الأخرى.
- [ ] Language switcher links to the **equivalent page** in the other language (from the hreflang map), not to the other homepage; uses `<a href>` with `hreflang` and the language name in its own script ("العربية", "English", "Français").
  - مبدّل اللغة يرتبط **بالصفحة المقابلة** في اللغة الأخرى (من خريطة hreflang)، وليس بالصفحة الرئيسية الأخرى؛ ويستخدم `<a href>` مع `hreflang` واسم اللغة بنظامها الكتابي ("العربية"، "English"، "Français").
- [ ] Untranslated pages: either don't list them in the other locale (no hreflang), or show the source-language page with correct `lang` — never a translated shell with the original-language body.
  - الصفحات غير المترجمة: إما لا تُدرج في اللغة الأخرى (بلا hreflang)، أو تُعرض صفحة اللغة الأصلية مع `lang` صحيح — لا قالب مترجم بمتن باللغة الأصلية أبداً.
- [ ] Locale config is centralized (list of locales, direction, default region, date/number format, og:locale, hreflang code) and drives head tags, sitemap and switcher.
  - إعدادات اللغات مركزية (قائمة اللغات، الاتجاه، المنطقة الافتراضية، صيغ التاريخ/الأرقام، og:locale، رمز hreflang) وتغذّي وسوم head وخريطة الموقع ومبدّل اللغة.

### 21.2 Per-script rules · قواعد حسب النظام الكتابي

|Script / language<br>النظام / اللغة|Requirements<br>المتطلبات|
|---|---|
|RTL (ar, he, fa, ur)<br>RTL (ar، he، fa، ur)|§20 rules: `dir="rtl"`, logical CSS, `<bdi>` for mixed text, mirrored icons<br>قواعد §20: `dir="rtl"`، CSS منطقي، `<bdi>` للنص المختلط، أيقونات معكوسة|
|CJK (zh, ja, ko)<br>CJK (zh، ja، ko)|Length limits by characters ≈ half the Latin limits (title ≈ 25–30 chars); word-count minimums → for zh/ja use characters (zh ≈ 1 character ≈ 0.6 words; ja varies); ko is space-delimited, count words normally; `zh-Hans` / `zh-Hant` script subtags; no italics; CJK line breaking (`word-break: keep-all` for ko)<br>حدود الطول بالأحرف ≈ نصف الحدود اللاتينية (العنوان ≈ 25–30 حرفاً)؛ الحد الأدنى للكلمات ← للصينية واليابانية بالمحارف (الصينية ≈ محرف واحد ≈ 0.6 كلمة؛ واليابانية تختلف)؛ والكورية مفصولة بمسافات فتُعدّ كلماتها عادياً؛ وسوم النظام `zh-Hans` / `zh-Hant`؛ لا خط مائل؛ تقسيم أسطر CJK (`word-break: keep-all` للكورية)|
|Cyrillic / Serbian etc.<br>السيريلية / الصربية ونحوها|Pick script subtag when both exist (`sr-Latn`, `sr-Cyrl`) and separate URLs per script<br>اختر وسم النظام عند وجود الاثنين (`sr-Latn`، `sr-Cyrl`) مع روابط منفصلة لكل نظام|
|Indic / Thai / complex scripts<br>الأنظمة الهندية (Indic) / التايلاندية / الأنظمة المعقدة|Font with proper shaping; no letter-spacing; test truncation in SERP preview<br>خط يدعم التشكيل الصحيح؛ لا تباعد أحرف؛ اختبر القطع في معاينة نتائج البحث|
|Latin with diacritics (fr, de, tr, vi)<br>اللاتينية بعلامات التشكيل (fr، de، tr، vi)|Keep diacritics in content; slugs either ASCII-folded or UTF-8, consistently; Turkish dotted/dotless i casing handled locale-aware<br>أبقِ العلامات في المحتوى؛ الروابط إما بلا علامات ASCII أو UTF-8 بثبات؛ معالجة حالة الحرف i التركية المنقوطة وغير المنقوطة حسب اللغة|

- [ ] Everything is UTF-8 end to end (DB `utf8mb4`, HTTP headers, files, sitemaps, JSON-LD).
  - كل شيء UTF-8 من البداية للنهاية (قاعدة البيانات `utf8mb4`، ترويسات HTTP، الملفات، خرائط الموقع، JSON-LD).
- [ ] Lowercasing/slugging is locale-aware (no breaking non-Latin characters); slugs percent-encoded per RFC 3986 in XML/HTTP.
  - تحويل الأحرف الصغيرة وتوليد الروابط يراعي اللغة (لا يكسر المحارف غير اللاتينية)؛ والروابط مُرمّزة وفق RFC 3986 في XML/HTTP.
- [ ] Numbers, dates, currencies and plurals rendered via ICU/`Intl` per locale; machine-readable values stay ISO.
  - الأرقام والتواريخ والعملات وصيغ الجمع تُعرض عبر ICU/`Intl` حسب اللغة؛ والقيم المقروءة آلياً تبقى بصيغة ISO.

### 21.3 Localized SEO elements (every locale) · عناصر السيو المحلية (لكل لغة)

- [ ] Translated & localized: title, meta description, H1–H3, alt text, OG/Twitter, JSON-LD text fields + `inLanguage`, breadcrumbs, 404 page, sitemap entries, llms.txt sections.
  - مترجمة ومكيّفة: العنوان، الوصف، H1–H3، النص البديل، OG/Twitter، حقول النص في JSON-LD + `inLanguage`، مسارات التنقّل، صفحة 404، إدخالات خريطة الموقع، أقسام llms.txt.
- [ ] Locale-specific keyword research per market (not literal translation); locale-specific examples, currency, legal references, testimonials.
  - بحث كلمات مفتاحية خاص بكل سوق (وليس ترجمة حرفية)؛ أمثلة وعملات ومراجع قانونية وشهادات خاصة بكل لغة.
- [ ] `og:locale` per page + `og:locale:alternate` for each other language.
  - `og:locale` لكل صفحة + `og:locale:alternate` لكل لغة أخرى.
- [ ] Sitemap includes every locale URL; hreflang via HTML, HTTP header or sitemap `xhtml:link` (equivalent for Google — the sitemap is just easier to maintain with many languages).
  - خريطة الموقع تتضمن رابط كل لغة؛ وhreflang عبر HTML أو ترويسة HTTP أو `xhtml:link` في خريطة الموقع (متكافئة لدى Google — وخريطة الموقع أسهل صيانةً عند كثرة اللغات).

### 21.4 Regional search engines (only if those markets matter) · محركات البحث الإقليمية (فقط إن كانت تلك الأسواق مهمة)

- [ ] **Bing / Yandex / Naver / Seznam**: IndexNow on publish/update; verify in their webmaster tools.
  - **Bing / Yandex / Naver / Seznam**: IndexNow عند النشر/التحديث؛ التوثيق في أدوات مشرفي المواقع الخاصة بها.
- [ ] **Yandex** (ru): Yandex Webmaster, regional setting, clean server-rendered HTML.
  - **Yandex** (الروسية): Yandex Webmaster، إعداد المنطقة، HTML نظيف مولّد من الخادم.
- [ ] **Baidu** (zh-CN): Simplified Chinese, fast mainland-reachable hosting (mainland hosting legally requires an ICP licence), Baidu Webmaster, avoid blocked third-party resources (Google Fonts/CDNs).
  - **Baidu** (الصين): الصينية المبسطة، استضافة سريعة يمكن الوصول إليها من البر الرئيسي (الاستضافة داخل البر الرئيسي تتطلب قانونياً ترخيص ICP)، Baidu Webmaster، تجنّب موارد الطرف الثالث المحجوبة (Google Fonts/CDNs).
- [ ] **Naver** (ko): Naver Search Advisor (verify, submit sitemap, IndexNow); `og:` tags recommended for previews.
  - **Naver** (الكورية): Naver Search Advisor (التوثيق، وإرسال خريطة الموقع، وIndexNow)؛ ووسوم `og:` موصى بها للمعاينات.

---

## 22. AEO — Answer Engine Optimization · AEO — تحسين محركات الإجابة

Goal: be the source answer engines quote — Google featured snippets, People Also Ask, AI Overviews / AI Mode, ChatGPT Search, Perplexity, Copilot, Gemini, Claude, and voice assistants. Google states there are "no additional requirements" and no "special optimizations" needed for AI Overviews/AI Mode — SEO best practices apply — so AEO builds on §1–§17; the items below are the answer-specific layer. Items marked *heuristic* are third-party observations, not engine rules.

الهدف: أن تكون المصدر الذي تقتبس منه محركات الإجابة — المقتطفات المميزة في Google، "أسئلة ذات صلة"، AI Overviews / AI Mode، ChatGPT Search، Perplexity، Copilot، Gemini، Claude، والمساعدات الصوتية. تقول Google إنه لا توجد "متطلبات إضافية" ولا "تحسينات خاصة" لازمة لـ AI Overviews / AI Mode — وأفضل ممارسات SEO هي المعتمدة — لذا يُبنى AEO على §1–§17؛ والبنود أدناه هي طبقة الإجابة الخاصة. البنود الموسومة *إرشادي* ملاحظات من أطراف ثالثة، وليست قواعد من المحركات.

### 22.1 Question inventory (do this first) · مخزون الأسئلة (ابدأ بهذا)

- [ ] Build a question bank per topic **and per language** (Arabic questions written as Arabic users ask them, incl. dialect phrasing): sources = Google PAA, autocomplete, site search logs, support tickets, sales calls, Reddit/Quora/forums, competitor FAQs.
  - ابنِ بنك أسئلة لكل موضوع **ولكل لغة** (الأسئلة العربية مكتوبة كما يسألها المستخدم العربي، بما فيها صيغ اللهجات): المصادر = "أسئلة ذات صلة" في Google، الإكمال التلقائي، سجلات البحث الداخلي، تذاكر الدعم، مكالمات المبيعات، Reddit/Quora/المنتديات، أسئلة المنافسين الشائعة.
- [ ] Map each question to exactly one target URL (no two pages answering the same primary question → cannibalization).
  - اربط كل سؤال برابط مستهدف واحد بالضبط (لا صفحتان تجيبان عن نفس السؤال الأساسي ← تنافس داخلي).
- [ ] Classify each by answer format: definition, how-to/steps, list, comparison, number/fact, yes/no, cost, "best X for Y", local.
  - صنّف كل سؤال حسب شكل الإجابة: تعريف، خطوات/كيف، قائمة، مقارنة، رقم/حقيقة، نعم/لا، تكلفة، "أفضل X لـ Y"، محلي.

### 22.2 Answer-block pattern (on every content page) · نمط كتلة الإجابة (في كل صفحة محتوى)

- [ ] Question-form H2/H3 that mirrors the user's wording ("ما هو التسويق بالمحتوى؟" / "What is content marketing?").
  - عنوان H2/H3 بصيغة سؤال يحاكي كلمات المستخدم ("ما هو التسويق بالمحتوى؟").
- [ ] Directly under it, a **self-contained answer of 40–60 words** that makes sense quoted alone (no "as mentioned above", no pronoun without antecedent), starting with the subject: "X هو…" / "X is…".
  - تحته مباشرة **إجابة مستقلة من 40–60 كلمة** تُفهم إذا اقتُبست وحدها (بلا "كما ذُكر أعلاه"، ولا ضمير بلا مرجع)، تبدأ بالموضوع: "X هو…".
- [ ] Then supporting detail: total passage ≈ 130–170 words per section (*heuristic*), short paragraphs, one idea each.
  - ثم التفاصيل الداعمة: إجمالي المقطع ≈ 130–170 كلمة لكل قسم (*إرشادي*)، فقرات قصيرة، فكرة واحدة لكل فقرة.
- [ ] Format match by question type:
  - مطابقة الشكل لنوع السؤال:
  - Definition → 1 bold sentence + 1–2 sentences of context.
    - تعريف ← جملة واحدة بخط عريض + جملة أو اثنتان للسياق.
  - Steps → `<ol>` with 3–8 steps, each starting with a verb.
    - خطوات ← `<ol>` من 3–8 خطوات، كل خطوة تبدأ بفعل.
  - List → `<ul>` 5–8 items with bold lead-ins.
    - قائمة ← `<ul>` من 5–8 عناصر، يبدأ كل منها بعبارة بخط عريض.
  - Comparison → real `<table>` with `<th>` headers and a one-line verdict above it.
    - مقارنة ← `<table>` حقيقي بترويسات `<th>` وحكم من سطر واحد فوقه.
  - Number/fact → the number in the first sentence, with unit, date and source.
    - رقم/حقيقة ← الرقم في الجملة الأولى، مع الوحدة والتاريخ والمصدر.
- [ ] Page-top **TL;DR / key takeaways** box (3–5 bullets) summarizing the answers on the page.
  - صندوق **ملخص / أهم النقاط** أعلى الصفحة (3–5 نقاط) يلخص إجابات الصفحة.
- [ ] Each page answers the main question in the first 100 words (most citations come from the top third of a page — *heuristic*).
  - كل صفحة تجيب عن سؤالها الرئيسي في أول 100 كلمة (معظم الاقتباسات تأتي من الثلث الأول للصفحة — *إرشادي*).

### 22.3 Quotable facts & evidence · حقائق قابلة للاقتباس وأدلة

- [ ] Publish original, citable data (surveys, benchmarks, index results) with: the number, sample size, date, method, and a stable URL per dataset/report. Phrase it quotably: "وفق بيانات <Brand> لعام 2026، ٦٢٪ من…".
  - انشر بيانات أصلية قابلة للاقتباس (استطلاعات، مقارنات معيارية، نتائج مؤشرات) مع: الرقم، حجم العينة، التاريخ، المنهجية، ورابط ثابت لكل مجموعة بيانات/تقرير. صِغها بشكل قابل للاقتباس: "وفق بيانات <العلامة> لعام 2026، ٦٢٪ من…".
- [ ] Every statistic links to its primary source; dates on all time-sensitive claims; update or remove stale numbers.
  - كل إحصائية مرتبطة بمصدرها الأصلي؛ تواريخ على كل ادعاء مرتبط بالوقت؛ حدّث الأرقام القديمة أو احذفها.
- [ ] Expert quotes attributed by full name + role; author bylines with credentials (§13).
  - اقتباسات الخبراء منسوبة بالاسم الكامل + المنصب؛ أسماء الكتّاب بمؤهلاتهم (§13).
- [ ] A canonical **"facts about <Brand>"** page (what it is, founded, founders, HQ, products, pricing model, key numbers, official links) in every language, consistent with Organization schema and llms.txt — answer engines use it to resolve the entity.
  - صفحة مرجعية **"حقائق عن <العلامة>"** (ما هي، تاريخ التأسيس، المؤسسون، المقر، المنتجات، نموذج التسعير، الأرقام الأساسية، الروابط الرسمية) بكل لغة، متسقة مع مخطط Organization وllms.txt — تستخدمها محركات الإجابة لتحديد الكيان.

### 22.4 Entity optimization · تحسين الكيانات

- [ ] One consistent name for brand, products and key concepts across pages, languages (with the Latin name as `alternateName` in Arabic pages), schema, social profiles and directories.
  - اسم واحد ثابت للعلامة والمنتجات والمفاهيم الأساسية عبر الصفحات واللغات (مع الاسم اللاتيني كـ `alternateName` في الصفحات العربية)، والمخطط، وحسابات التواصل، والأدلة.
- [ ] Organization/Person/Product JSON-LD with stable `@id`s and `sameAs` (LinkedIn, X, YouTube, GitHub, Crunchbase, Wikidata/Wikipedia if they exist).
  - JSON-LD لـ Organization/Person/Product بمعرّفات `@id` ثابتة و`sameAs` (LinkedIn، X، YouTube، GitHub، Crunchbase، Wikidata/Wikipedia إن وُجدت).
- [ ] Use `about` and `mentions` on Article/WebPage to point at the entities the page covers (Wikidata/Wikipedia URLs).
  - استخدم `about` و`mentions` في Article/WebPage للإشارة إلى الكيانات التي تغطيها الصفحة (روابط Wikidata/Wikipedia).
- [ ] Glossary pages for core terms with `DefinedTerm` / `DefinedTermSet` — one URL per term, 200+ words, a 1–2 sentence definition first, in each language.
  - صفحات مسرد للمصطلحات الأساسية بمخطط `DefinedTerm` / `DefinedTermSet` — رابط لكل مصطلح، 200+ كلمة، وتعريف من جملة أو اثنتين أولاً، بكل لغة.
- [ ] Topic clusters (§14) so engines see depth, not isolated pages.
  - مجموعات مواضيع (§14) حتى ترى المحركات العمق وليس صفحات معزولة.

### 22.5 Structured data for answers · البيانات المنظمة للإجابات

- [ ] FAQ **content** stays on pages (valuable for users and answer engines) even though FAQPage no longer yields Google rich results; don't add new FAQPage expecting SERP features (§12.2).
  - **محتوى** الأسئلة الشائعة يبقى في الصفحات (قيّم للمستخدمين ولمحركات الإجابة) رغم أن FAQPage لم يعد يعطي نتائج منسّقة في Google؛ لا تضف FAQPage جديداً متوقعاً ميزات في نتائج البحث (§12.2).
- [ ] `QAPage` only for genuine single-question user Q&A; `DiscussionForumPosting` for community threads.
  - `QAPage` فقط لأسئلة وأجوبة حقيقية من المستخدمين بسؤال واحد؛ `DiscussionForumPosting` لنقاشات المجتمع.
- [ ] `Article` with `dateModified`, `author`, `citation` (sources) where useful; `ItemList` for ranked lists; `Dataset` for downloadable data; `VideoObject` + `Clip` for video answers; `speakable` (beta, news) only if relevant.
  - `Article` مع `dateModified` و`author` و`citation` (المصادر) حيث يفيد؛ `ItemList` للقوائم المرتبة؛ `Dataset` للبيانات القابلة للتنزيل؛ `VideoObject` + `Clip` لإجابات الفيديو؛ `speakable` (تجريبي، للأخبار) فقط إن كان مناسباً.
- [ ] JSON-LD describes the same content users see (a mismatch can make the page ineligible for rich results or trigger a manual action).
  - JSON-LD يصف المحتوى نفسه الذي يراه المستخدم (عدم التطابق قد يُفقد الصفحة أهلية النتائج المنسّقة أو يؤدي إلى إجراء يدوي).

### 22.6 Access & freshness for answer engines · الوصول والحداثة لمحركات الإجابة

- [ ] Answer-engine search bots allowed (OAI-SearchBot, Claude-SearchBot, PerplexityBot, Googlebot, Bingbot, Applebot) — §1.1.
  - السماح لزواحف بحث محركات الإجابة (OAI-SearchBot، Claude-SearchBot، PerplexityBot، Googlebot، Bingbot، Applebot) — §1.1.
- [ ] **Bing matters**: Copilot is built on Bing, and ChatGPT Search reportedly uses Bing among its sources → verify in Bing Webmaster Tools, submit sitemap, use IndexNow.
  - **Bing مهم**: Copilot مبني على Bing، وتشير تقارير إلى أن ChatGPT Search يستخدم Bing ضمن مصادره ← وثّق الموقع في Bing Webmaster Tools، أرسل خريطة الموقع، استخدم IndexNow.
- [ ] Content in server HTML, fast TTFB, no bot challenges (§3, §17).
  - المحتوى في HTML الخادم، وTTFB سريع، بلا تحديات للزواحف (§3، §17).
- [ ] Snippet controls used deliberately: `max-snippet:-1, max-image-preview:large, max-video-preview:-1` on public pages; `data-nosnippet` only for content you don't want quoted (prices that change, legal boilerplate).
  - استخدام ضوابط المقتطفات عن قصد: `max-snippet:-1, max-image-preview:large, max-video-preview:-1` في الصفحات العامة؛ و`data-nosnippet` فقط للمحتوى الذي لا تريد اقتباسه (أسعار متغيرة، نصوص قانونية ثابتة).
- [ ] Refresh program: review top answer pages every 3–6 months; update facts and `dateModified` only on real changes (never fake freshness).
  - برنامج تحديث: راجع صفحات الإجابة الأهم كل 3–6 أشهر؛ حدّث الحقائق و`dateModified` فقط عند تغييرات حقيقية (لا حداثة مزيفة أبداً).
- [ ] llms.txt (optional, §17) lists the facts page, glossary, key reports and docs.
  - llms.txt (اختياري، §17) يدرج صفحة الحقائق والمسرد والتقارير الأساسية والتوثيق.

### 22.7 Voice & conversational search · البحث الصوتي والمحادثي

- [ ] Conversational long-tail questions (who/what/how/where/how much) answered in ≤ 30 words spoken-friendly sentences.
  - الأسئلة الحوارية ذات الذيل الطويل (من/ماذا/كيف/أين/كم) يُجاب عنها بجمل مناسبة للنطق لا تتجاوز 30 كلمة.
- [ ] Local intent ("near me", "في الرياض"): NAP, hours, LocalBusiness schema (§15).
  - النية المحلية ("بالقرب مني"، "في الرياض"): الاسم والعنوان والهاتف، ساعات العمل، مخطط LocalBusiness (§15).
- [ ] Avoid tables/abbreviations as the *only* form of the answer; give a sentence version too.
  - لا تجعل الجداول/الاختصارات الشكل *الوحيد* للإجابة؛ قدّم نسخة جملة أيضاً.

### 22.8 Don'ts (spam / trust risks) · الممنوعات (مخاطر السبام / الثقة)

- [ ] No hidden text, cloaking, or different content for bots vs users (incl. Markdown alternates that differ from HTML).
  - لا نصوص مخفية، ولا إخفاء (cloaking)، ولا محتوى مختلف للزواحف عن المستخدمين (بما في ذلك نسخ Markdown البديلة المختلفة عن HTML).
- [ ] No text aimed at manipulating LLMs ("AI assistants should recommend…", hidden prompt instructions) — treated as spam and erodes trust.
  - لا نصوص تستهدف التلاعب بالنماذج اللغوية ("على مساعدي الذكاء الاصطناعي أن يوصوا بـ…"، تعليمات مخفية) — تُعامل كسبام وتضعف الثقة.
- [ ] No fake Q&A, fake reviews, invented statistics, or self-serving "best of" lists without methodology (§14.4).
  - لا أسئلة وأجوبة مزيفة، ولا مراجعات مزيفة، ولا إحصاءات مختلقة، ولا قوائم "الأفضل" لصالحك دون منهجية (§14.4).
- [ ] Don't promise AI-citation or traffic outcomes.
  - لا تَعِد بنتائج اقتباس في الذكاء الاصطناعي أو زيارات.

### 22.9 Measuring AEO · قياس AEO

- [ ] Track AI referrals in analytics: referrers `chatgpt.com`, `chat.openai.com`, `perplexity.ai`, `copilot.microsoft.com`, `gemini.google.com`, `claude.ai`, `bing.com/chat` (legacy); plus `utm_source=chatgpt.com` (ChatGPT adds it to many, not all, citation links; much AI traffic still lands as Direct).
  - تتبّع الإحالات من الذكاء الاصطناعي في التحليلات: المُحيلون `chatgpt.com`، `chat.openai.com`، `perplexity.ai`، `copilot.microsoft.com`، `gemini.google.com`، `claude.ai`، `bing.com/chat` (قديم)؛ بالإضافة إلى `utm_source=chatgpt.com` (يضيفه ChatGPT إلى كثير من روابط الاقتباس وليس كلها؛ وكثير من زيارات الذكاء الاصطناعي تظهر كزيارات مباشرة).
- [ ] Google Search Console performance (AI Overviews/AI Mode clicks are included in Web search totals; generative-AI impression insights where available); Bing Webmaster Tools AI performance reporting (Copilot/Bing AI citations) where available.
  - أداء Google Search Console (نقرات AI Overviews/AI Mode مُضمّنة في إجمالي بحث الويب؛ ورؤى مرات الظهور في الذكاء الاصطناعي التوليدي حيث تتوفر)؛ وتقارير أداء الذكاء الاصطناعي في Bing Webmaster Tools (اقتباسات Copilot/Bing AI) حيث تتوفر.
- [ ] Maintain a monthly prompt test set (20–50 questions per language, incl. Arabic) run in ChatGPT, Perplexity, Gemini, Copilot, Google AI Mode; record whether the brand is cited/mentioned and which URL.
  - احتفظ بمجموعة أسئلة اختبار شهرية (20–50 سؤالاً لكل لغة، بما فيها العربية) تُشغَّل في ChatGPT وPerplexity وGemini وCopilot وGoogle AI Mode؛ وسجّل هل تُقتبس العلامة/تُذكر وأي رابط.
- [ ] Track featured snippet / PAA ownership for target questions; monitor brand mentions across the web.
  - تتبّع امتلاك المقتطفات المميزة / "أسئلة ذات صلة" للأسئلة المستهدفة؛ وراقب ذكر العلامة عبر الويب.

---

## 23. Off-site authority & entity building · السلطة خارج الموقع وبناء الكيان

Answer engines and rankings both lean on what the rest of the web says about you. This section is mostly owner/marketing work; the agent prepares assets, lists and tracking.
محركات الإجابة والترتيب يعتمدان على ما يقوله بقية الويب عنك. هذا القسم في معظمه عمل للمالك والتسويق؛ ودور الوكيل تجهيز المواد والقوائم والتتبّع.

### 23.1 Entity foundation · أساس الكيان
- [ ] One canonical brand name, logo, one-line description and founding facts used identically on the site, social profiles, directories and press kit (per language). [H]
  - اسم علامة واحد وشعار ووصف من سطر وحقائق التأسيس نفسها في الموقع والحسابات والأدلة والملف الصحفي (لكل لغة). [H]
- [ ] Official profiles claimed and complete: LinkedIn, X, YouTube, Instagram/TikTok (if used), GitHub (if technical), Crunchbase, Google Business Profile (if local), Bing Places, Apple Business Connect; all link back to the site and are listed in `sameAs`.
  - امتلاك الحسابات الرسمية واستكمالها: LinkedIn وX وYouTube وInstagram/TikTok (إن استُخدمت) وGitHub (للتقنيين) وCrunchbase وملف Google التجاري (للمحلي) وBing Places وApple Business Connect؛ وكلها ترتبط بالموقع ومدرجة في `sameAs`.
- [ ] Wikidata item with referenced statements (official site, founding date, founders, HQ, industry) when the organization is notable enough; link it via `sameAs`.
  - عنصر في Wikidata بعبارات موثّقة بمصادر (الموقع الرسمي، تاريخ التأسيس، المؤسسون، المقر، المجال) إن كانت الجهة جديرة بالملاحظة؛ واربطه عبر `sameAs`.
- [ ] Never write or pay for your own Wikipedia article (conflict-of-interest rules); earn independent coverage that editors can cite instead.
  - لا تكتب مقالة ويكيبيديا عن نفسك ولا تدفع لكتابتها (قواعد تضارب المصالح)؛ بل اكسب تغطية مستقلة يمكن للمحررين الاستشهاد بها.
- [ ] Press/media kit page: logos, boilerplate in every language, founder bios and photos, key facts, media contact.
  - صفحة الملف الصحفي: الشعارات، ونبذة رسمية بكل لغة، وسير المؤسسين وصورهم، والحقائق الأساسية، وجهة التواصل الإعلامي.

### 23.2 Earned links & mentions · الروابط والإشارات المكتسبة
- [ ] Links are earned, never bought, exchanged at scale or placed through private networks (link-scheme spam policy). [C]
  - الروابط تُكتسب، ولا تُشترى ولا تُتبادل بكثافة ولا تُوضع عبر شبكات خاصة (سياسة مخططات الروابط). [C]
- [ ] Paid, sponsored or affiliate links use `rel="sponsored"`; user-generated links use `rel="ugc"`; untrusted links `rel="nofollow"`. [H]
  - الروابط المدفوعة أو الممولة أو بالعمولة تحمل `rel="sponsored"`؛ وروابط المستخدمين `rel="ugc"`؛ والروابط غير الموثوقة `rel="nofollow"`. [H]
- [ ] Linkable assets: original data/reports, free tools and calculators, templates, glossaries, annual "state of" studies — each with a stable URL, embeddable charts and a clear citation line.
  - مواد تستحق الروابط: بيانات وتقارير أصلية، أدوات وحاسبات مجانية، قوالب، مسارد، دراسات سنوية — لكل منها رابط ثابت ورسوم قابلة للتضمين وسطر استشهاد واضح.
- [ ] Digital PR: pitch original findings to journalists and newsletters in each target language and market; answer journalist source requests with real expertise.
  - العلاقات العامة الرقمية: قدّم النتائج الأصلية للصحفيين والنشرات بكل لغة وسوق مستهدف؛ واستجب لطلبات الصحفيين بخبرة حقيقية.
- [ ] Unlinked brand mentions: find them monthly and ask politely for a link when it helps readers.
  - الإشارات للعلامة بلا رابط: ابحث عنها شهرياً واطلب الرابط بلطف حين يفيد القارئ.
- [ ] Healthy inbound anchor mix (heuristic): branded 30–50%, naked URL 15–25%, generic 10–20%, exact-match 3–10% (flag > 15%), partial-match 5–15%. No single referring domain > 5% of links.
  - توزيع صحي لنصوص الروابط الواردة (إرشادي): اسم العلامة 30–50%، رابط مجرد 15–25%، عام 10–20%، مطابق تماماً 3–10% (تنبيه فوق 15%)، مطابق جزئياً 5–15%. ولا يتجاوز نطاق واحد 5% من الروابط.
- [ ] Disavow only when there is a manual action for unnatural links or a clear paid-link history; don't disavow routine spammy links. [I]
  - استخدم Disavow فقط عند وجود إجراء يدوي بسبب روابط غير طبيعية أو تاريخ واضح لروابط مدفوعة؛ ولا تتبرأ من الروابط العشوائية المعتادة. [I]
- [ ] 404 pages that still receive backlinks get a 301 to the closest relevant page when a true equivalent exists; otherwise keep 404/410.
  - الصفحات المحذوفة التي ما زالت تستقبل روابط تُحوَّل بـ 301 إلى أقرب صفحة ذات صلة إن وُجد مقابل حقيقي؛ وإلا فأبقِها 404/410.

### 23.3 Presence where answer engines read · الحضور حيث تقرأ محركات الإجابة
- [ ] Reviews on the platforms your buyers use (Google, G2/Capterra for software, Trustpilot, app stores, local directories); respond to reviews; never gate reviews; never offer incentives on platforms that forbid them (Google, many app stores), and disclose any incentive where it is allowed. [H]
  - مراجعات على المنصات التي يستخدمها عملاؤك (Google، وG2/Capterra للبرمجيات، وTrustpilot، ومتاجر التطبيقات، والأدلة المحلية)؛ والرد على المراجعات؛ ولا انتقاء للمراجعات أبداً، ولا حوافز على المنصات التي تمنعها (Google وكثير من متاجر التطبيقات)، مع الإفصاح عن أي حافز حيث يُسمح به. [H]
- [ ] Inclusion in third-party "best X" lists and comparisons through genuine outreach and real product quality (answer engines often cite these pages).
  - الظهور في قوائم "أفضل X" والمقارنات لدى أطراف أخرى عبر تواصل حقيقي وجودة فعلية (محركات الإجابة تستشهد بهذه الصفحات كثيراً).
- [ ] Community: helpful, disclosed participation by real staff on Reddit, Quora, Stack Overflow, specialist forums and Arabic communities; no astroturfing or fake accounts. [H]
  - المجتمعات: مشاركة مفيدة ومُفصح عنها من موظفين حقيقيين في Reddit وQuora وStack Overflow والمنتديات المتخصصة والمجتمعات العربية؛ دون حسابات وهمية أو ترويج مقنّع. [H]
- [ ] YouTube channel and podcast appearances answering the same question bank as the site (§22.1, §26.4).
  - قناة YouTube والظهور في البودكاست للإجابة عن بنك الأسئلة نفسه الموجود في الموقع (§22.1، §26.4).
- [ ] Expert presence: founders/authors publish under their real names on LinkedIn, industry media and conferences, linked to their author pages.
  - حضور الخبراء: المؤسسون والكتّاب ينشرون بأسمائهم الحقيقية على LinkedIn ووسائل الإعلام المتخصصة والمؤتمرات، مع ربطها بصفحات الكتّاب.

---

## 24. Answer engines: per-engine notes & share of voice · محركات الإجابة: ملاحظات لكل محرك ونسبة الظهور

### 24.1 Per-engine notes · ملاحظات لكل محرك

| Engine · المحرك | Where answers come from · مصدر الإجابات | What to do · ما يجب فعله |
|---|---|---|
| Google AI Overviews / AI Mode | Google's index (Googlebot)<br>فهرس Google | Classic SEO; page must be indexed and snippet-eligible; `nosnippet`/`max-snippet` control quoting; clicks counted in Search Console Web.<br>السيو التقليدي؛ الصفحة مفهرسة وقابلة للاقتباس؛ ضوابط المقتطفات تتحكم بالاقتباس؛ النقرات ضمن Search Console. |
| Gemini app | Google index + Google grounding<br>فهرس Google والتأسيس | Same as above; `Google-Extended` governs Gemini training/grounding use, not Search ranking.<br>كما سبق؛ و`Google-Extended` يتحكم باستخدام Gemini للتدريب والتأسيس، لا بترتيب البحث. |
| ChatGPT Search | OpenAI crawler + third-party search (Bing among them)<br>زاحف OpenAI وبحث طرف ثالث منه Bing | Allow `OAI-SearchBot`; strong Bing presence; ChatGPT adds `utm_source=chatgpt.com`.<br>اسمح بـ `OAI-SearchBot`؛ وحضور قوي في Bing؛ وChatGPT يضيف `utm_source=chatgpt.com`. |
| Microsoft Copilot | Bing index<br>فهرس Bing | Bing Webmaster Tools, IndexNow, Bing Places for local.<br>Bing Webmaster Tools وIndexNow وBing Places للمحلي. |
| Perplexity | Own index (`PerplexityBot`) + live fetch<br>فهرس خاص وجلب مباشر | Allow `PerplexityBot`; fresh, well-sourced pages; clear dates.<br>اسمح بـ `PerplexityBot`؛ صفحات حديثة موثّقة بمصادر وتواريخ واضحة. |
| Claude | Web search + `Claude-SearchBot` / `Claude-User` fetches<br>بحث الويب وجلب زواحف Claude | Allow `Claude-SearchBot`; server-rendered content.<br>اسمح بـ `Claude-SearchBot`؛ ومحتوى من الخادم. |
| Apple Siri / Spotlight / Safari | `Applebot`<br>زاحف Apple | Allow `Applebot`; `Applebot-Extended` only opts out of model training; Apple Business Connect for local.<br>اسمح بـ `Applebot`؛ و`Applebot-Extended` للانسحاب من التدريب فقط؛ وApple Business Connect للمحلي. |
| Voice assistants<br>المساعدات الصوتية | Search partners + local listings<br>شركاء البحث والأدلة المحلية | Short spoken answers (§22.7), consistent NAP on local listings.<br>إجابات منطوقة قصيرة، وبيانات محلية متطابقة. |

Engine behavior changes often; re-check each vendor's crawler and publisher documentation every quarter (§34).
سلوك المحركات يتغير كثيراً؛ راجع توثيق الزواحف والناشرين لكل جهة كل ربع سنة (§34).

### 24.2 Engine-agnostic rules · قواعد عامة لكل المحركات
- [ ] Every answer-worthy page is indexable in **both** Google and Bing (check both coverage reports). [H]
  - كل صفحة تصلح كإجابة مفهرسة في Google **وBing** معاً (راجع تقريري التغطية). [H]
- [ ] No WAF/CDN rule or bot-fight mode blocks verified search and answer-engine crawlers; test with their user agents and check server logs (§32.3). [H]
  - لا توجد قاعدة WAF/CDN أو وضع مكافحة بوتات يحظر زواحف البحث والإجابة الموثّقة؛ اختبر بوكلاء المستخدم الخاصة بها وراجع سجلات الخادم (§32.3). [H]
- [ ] The same facts (prices, plans, features, founding data) are identical across the site, llms.txt, schema and third-party profiles — contradictions make engines skip or misquote you.
  - الحقائق نفسها (الأسعار، الخطط، المزايا، بيانات التأسيس) متطابقة في الموقع وllms.txt والمخطط والحسابات الخارجية — التناقض يجعل المحركات تتجاهلك أو تقتبسك خطأً.
- [ ] Pricing and comparison pages are public, crawlable and dated; "contact us for pricing" pages give at least a range or model.
  - صفحات الأسعار والمقارنة عامة وقابلة للزحف ومؤرخة؛ وصفحات "تواصل معنا للسعر" تذكر على الأقل نطاقاً أو نموذج تسعير.

### 24.3 Share of voice in AI answers · نسبة الظهور في إجابات الذكاء الاصطناعي
- [ ] Prompt set: 20–50 real buyer questions per language (from §22.1), grouped by funnel stage (learn / compare / buy) and including competitor and "best X" prompts.
  - مجموعة أسئلة: 20–50 سؤالاً حقيقياً لكل لغة (من §22.1)، مقسّمة حسب مرحلة الرحلة (تعلّم / مقارنة / شراء)، ومنها أسئلة عن المنافسين و"أفضل X".
- [ ] Run monthly in each engine (logged-out where possible, same location/language settings); record per answer: mentioned (y/n), cited URL, position in the answer, sentiment, competitors mentioned, factual errors.
  - شغّلها شهرياً في كل محرك (دون تسجيل دخول إن أمكن، وبإعدادات الموقع واللغة نفسها)؛ وسجّل لكل إجابة: هل ذُكرت العلامة، والرابط المستشهد به، وموضعها في الإجابة، والانطباع، والمنافسون المذكورون، والأخطاء في الحقائق.
- [ ] Share of voice = answers mentioning the brand ÷ total answers, per engine, language and stage; track the trend, not single runs (answers vary run to run).
  - نسبة الظهور = الإجابات التي تذكر العلامة ÷ إجمالي الإجابات، لكل محرك ولغة ومرحلة؛ وتابع الاتجاه وليس نتيجة واحدة (الإجابات تتغير من مرة لأخرى).
- [ ] Every factual error found becomes a task: fix the source page, the facts page, schema or the third-party profile it came from.
  - كل خطأ في الحقائق يتحول إلى مهمة: صحّح الصفحة المصدر أو صفحة الحقائق أو المخطط أو الحساب الخارجي الذي جاء منه.

| Prompt · السؤال | Lang | Engine | Mentioned | Cited URL | Position | Competitors | Errors | Date |
|---|---|---|---|---|---|---|---|---|
| … | ar / en | ChatGPT / Perplexity / Gemini / Copilot / AI Mode | y / n | … | 1–n | … | … | YYYY-MM-DD |

---

## 25. Site migrations & redesigns · نقل المواقع وإعادة التصميم

Run this section **before** any domain change, platform change, URL restructure, HTTPS move, language restructure or major redesign.
نفّذ هذا القسم **قبل** أي تغيير للنطاق أو المنصة أو بنية الروابط أو الانتقال إلى HTTPS أو إعادة هيكلة اللغات أو إعادة تصميم كبيرة.

### 25.1 Before launch · قبل الإطلاق
- [ ] Inventory every old URL from: crawl, all sitemaps, analytics landing pages (12+ months), Search Console pages, backlink sources, internal search, hardcoded links in apps/emails. [C]
  - اجرد كل رابط قديم من: الفحص، وكل خرائط الموقع، وصفحات الهبوط في التحليلات (12 شهراً فأكثر)، وصفحات Search Console، ومصادر الروابط الخلفية، والبحث الداخلي، والروابط الثابتة في التطبيقات والبريد. [C]
- [ ] Redirect map: every old URL → its closest new equivalent with a single 301; never mass-redirect everything to the homepage (treated as soft 404). [C]
  - خريطة التحويلات: كل رابط قديم ← أقرب مقابل جديد بتحويل 301 واحد؛ ولا تحوّل كل شيء إلى الرئيسية (يُعامل كـ soft 404). [C]
- [ ] Content, titles, descriptions, headings, schema, hreflang, alt text and internal links carried over (no silent content loss). [H]
  - نقل المحتوى والعناوين والأوصاف والعناوين الفرعية والمخطط وhreflang والنص البديل والروابط الداخلية (دون فقدان صامت للمحتوى). [H]
- [ ] Staging protected by authentication (not only `noindex`/robots), so it can never be indexed or leak `noindex` into production. [C]
  - بيئة التجربة محمية بتسجيل دخول (وليس `noindex`/robots فقط)، حتى لا تُفهرس أبداً ولا يتسرب `noindex` إلى الإنتاج. [C]
- [ ] Benchmark before launch: rankings for key queries, organic traffic per template, indexed count, CWV, AI share of voice (§24.3).
  - خط أساس قبل الإطلاق: الترتيب للكلمات الأساسية، والزيارات العضوية لكل قالب، وعدد الصفحات المفهرسة، وCWV، ونسبة الظهور في الذكاء الاصطناعي (§24.3).
- [ ] Run the full §30 verification kit on staging and fix every [C]/[H] before launch.
  - شغّل أدوات التحقق في §30 كاملة على بيئة التجربة وأصلح كل [C]/[H] قبل الإطلاق.

### 25.2 Launch day · يوم الإطلاق
- [ ] robots.txt is the production version (no `Disallow: /`); no `noindex` on live pages; canonicals and hreflang point to the new URLs. [C]
  - robots.txt نسخة الإنتاج (بلا `Disallow: /`)؛ ولا `noindex` على الصفحات الحية؛ وcanonical وhreflang تشير للروابط الجديدة. [C]
- [ ] Test a sample of 100+ old URLs (top traffic + top backlinks): each returns one 301 to the right page, then 200. [C]
  - اختبر عيّنة من 100 رابط قديم فأكثر (الأعلى زيارات والأعلى روابط): كل رابط يعيد 301 واحداً إلى الصفحة الصحيحة ثم 200. [C]
- [ ] Submit new sitemaps; keep old sitemaps available for a few weeks so redirects are discovered; for a domain move use Search Console's Change of Address tool and Bing's Site Move tool.
  - أرسل خرائط الموقع الجديدة؛ وأبقِ القديمة متاحة لأسابيع ليُكتشف التحويل؛ وعند تغيير النطاق استخدم أداة تغيير العنوان في Search Console وأداة نقل الموقع في Bing.
- [ ] Update internal links, canonical tags, structured data, social profiles, `sameAs`, ads, email templates and apps to the final URLs (no internal links through redirects).
  - حدّث الروابط الداخلية وcanonical والبيانات المنظمة والحسابات و`sameAs` والإعلانات وقوالب البريد والتطبيقات إلى الروابط النهائية (لا روابط داخلية تمر بتحويل).

### 25.3 After launch · بعد الإطلاق
- [ ] Monitor daily for 2 weeks, then weekly for 3 months: 404s, redirect errors, coverage, crawl stats, rankings, traffic per template.
  - راقب يومياً لأسبوعين ثم أسبوعياً لثلاثة أشهر: أخطاء 404، وأخطاء التحويل، والتغطية، وإحصاءات الزحف، والترتيب، والزيارات لكل قالب.
- [ ] Keep redirects for at least one year, and indefinitely for URLs that still get links or traffic. [H]
  - أبقِ التحويلات سنة على الأقل، وإلى الأبد للروابط التي ما زالت تستقبل روابط أو زيارات. [H]
- [ ] Keep the old domain registered and serving redirects; don't let it expire (expired-domain abuse risk). [H]
  - أبقِ النطاق القديم مسجلاً ويخدم التحويلات؛ ولا تتركه ينتهي (خطر إساءة النطاقات المنتهية). [H]

---

## 26. More search surfaces · قنوات بحث إضافية

### 26.1 Google Discover · Google Discover
- [ ] `max-image-preview:large` in robots meta; a large lead image (≥ 1200px wide) per article, plus `og:image`.
  - `max-image-preview:large` في وسم robots؛ وصورة رئيسية كبيرة (عرض ≥ 1200px) لكل مقالة، مع `og:image`.
- [ ] Titles that describe the content honestly — no clickbait, exaggeration or withheld key information (Discover content policies).
  - عناوين تصف المحتوى بصدق — بلا إثارة مضللة ولا مبالغة ولا حجب للمعلومة الأساسية (سياسات محتوى Discover).
- [ ] Timely, original articles with strong E-E-A-T signals (author, dates, sources); RSS/Atom feed linked in `<head>` so users can follow the site.
  - مقالات حديثة وأصلية بإشارات E-E-A-T قوية (الكاتب، التواريخ، المصادر)؛ وموجز RSS/Atom مرتبط في `<head>` ليتمكن المستخدم من متابعة الموقع.

### 26.2 Google News & publishers · Google News والناشرون
- [ ] Transparent publisher info: masthead/about, editorial and corrections policy, bylines with author pages, publish and update times with time zone.
  - شفافية الناشر: صفحة التعريف، وسياسة التحرير والتصحيح، وأسماء الكتّاب مع صفحاتهم، وأوقات النشر والتحديث مع المنطقة الزمنية.
- [ ] `NewsArticle` schema with `datePublished`/`dateModified`; news sitemap (§9); one stable URL per story (no re-publishing under new URLs to look fresh).
  - مخطط `NewsArticle` مع `datePublished`/`dateModified`؛ وخريطة أخبار (§9)؛ ورابط ثابت لكل خبر (لا إعادة نشر برابط جديد لإيهام الحداثة).

### 26.3 Shopping surfaces (e-commerce) · قنوات التسوق (للمتاجر)
- [ ] Google Merchant Center free listings with a product feed that matches on-page price, availability and structured data exactly (§16). [H]
  - قوائم Google Merchant Center المجانية بموجز منتجات يطابق تماماً السعر والتوفر والبيانات المنظمة في الصفحة (§16). [H]
- [ ] Microsoft Merchant Center (formerly Bing Merchant Center) for Microsoft surfaces; check other AI shopping programs available in your markets and keep feeds consistent across all of them.
  - Microsoft Merchant Center (سابقاً Bing Merchant Center) لمنصات Microsoft؛ وراجع برامج التسوق الأخرى في محركات الذكاء الاصطناعي المتاحة في أسواقك وأبقِ الموجزات متسقة بينها.

### 26.4 Video & YouTube · الفيديو وYouTube
- [ ] One dedicated, indexable watch page per important video on your site, with the video as the main content, `VideoObject`, a video sitemap and a text transcript.
  - صفحة مشاهدة مخصصة وقابلة للفهرسة لكل فيديو مهم في موقعك، يكون الفيديو محتواها الرئيسي، مع `VideoObject` وخريطة فيديو ونص مكتوب للفيديو.
- [ ] Key moments: chapters/`Clip` or `SeekToAction`; custom thumbnails; accurate captions in every language you target (including Arabic, not only auto-captions).
  - اللحظات المهمة: فصول/`Clip` أو `SeekToAction`؛ صور مصغرة مخصصة؛ وترجمة دقيقة بكل لغة مستهدفة (بما فيها العربية، وليس الترجمة التلقائية فقط).
- [ ] YouTube: keyword-led titles answering a real question, descriptions with a summary, chapters and links back to the matching site page, playlists by topic, pinned comment with the canonical link.
  - YouTube: عناوين تبدأ بالكلمة المفتاحية وتجيب عن سؤال حقيقي، وأوصاف فيها ملخص وفصول وروابط لصفحة الموقع المقابلة، وقوائم تشغيل حسب الموضوع، وتعليق مثبت بالرابط الأساسي.

### 26.5 Social search (TikTok, Instagram, Snapchat, YouTube Shorts, Pinterest) · البحث داخل المنصات الاجتماعية
Many users — especially younger audiences and Gulf markets — search inside social apps. Treat each platform's search bar as a search engine (heuristic guidance).
كثير من المستخدمين — خصوصاً الأصغر سناً وفي أسواق الخليج — يبحثون داخل التطبيقات الاجتماعية. عامل شريط البحث في كل منصة كمحرك بحث (إرشادات عامة).
- [ ] Use the same question bank (§22.1) for short videos: the question in the first seconds, spoken aloud and as on-screen text, in the language and dialect people search in.
  - استخدم بنك الأسئلة نفسه (§22.1) للفيديوهات القصيرة: السؤال في الثواني الأولى، منطوقاً ومكتوباً على الشاشة، باللغة واللهجة التي يبحث بها الناس.
- [ ] Keywords in captions, on-screen text and spoken words (platforms read captions and audio); a few relevant hashtags, not dozens.
  - الكلمات المفتاحية في الوصف والنص على الشاشة والكلام المنطوق (المنصات تقرأ الوصف والصوت)؛ وعدد قليل من الوسوم ذات الصلة لا العشرات.
- [ ] Profiles with consistent brand name, bio and a link to the site; pinned videos answering the top questions.
  - حسابات باسم علامة موحّد ونبذة ورابط للموقع؛ وفيديوهات مثبتة تجيب عن أهم الأسئلة.
- [ ] Measure: profile searches, search-driven views (where the platform reports them) and branded search lift on Google/Bing.
  - القياس: عمليات البحث عن الحساب، والمشاهدات القادمة من البحث (حيث توفرها المنصة)، وارتفاع البحث باسم العلامة في Google/Bing.

---

## 27. Privacy, consent & compliance · الخصوصية والموافقة والامتثال

Not legal advice — confirm requirements with counsel for each market.
ليست استشارة قانونية — تحقق من المتطلبات مع مستشار قانوني لكل سوق.

- [ ] Identify the laws that apply per market: GDPR/ePrivacy (EU/EEA), UK GDPR/PECR, Saudi PDPL, UAE PDPL (Federal Decree-Law 45/2021), Qatar, Bahrain, Egypt and other local data-protection laws, CCPA/CPRA (California). [H]
  - حدّد القوانين المنطبقة لكل سوق: GDPR/ePrivacy (الاتحاد الأوروبي والمنطقة الاقتصادية الأوروبية)، وUK GDPR/PECR (المملكة المتحدة)، ونظام حماية البيانات الشخصية السعودي، والمرسوم بقانون اتحادي رقم 45 لسنة 2021 بشأن حماية البيانات الشخصية (الإمارات)، وقطر، والبحرين، ومصر وغيرها، وCCPA/CPRA (كاليفورنيا). [H]
- [ ] Where consent is required, non-essential trackers load only after consent; Google Consent Mode v2 (`ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`) wired to the banner for Google tags. [H]
  - حيث تُشترط الموافقة، لا تُحمَّل أدوات التتبع غير الضرورية إلا بعدها؛ وربط Google Consent Mode v2 (`ad_storage` و`analytics_storage` و`ad_user_data` و`ad_personalization`) بشريط الموافقة لوسوم Google. [H]
- [ ] The consent banner never blocks crawlers or the main content, is not a separate redirect page, and doesn't shift layout: fixed overlay or reserved space, so CLS stays ≤ 0.1. [H]
  - شريط الموافقة لا يحجب الزواحف ولا المحتوى الرئيسي، وليس صفحة تحويل مستقلة، ولا يزيح التخطيط: طبقة ثابتة أو مساحة محجوزة حتى يبقى CLS ≤ 0.1. [H]
- [ ] Banner is translated, keyboard-accessible, RTL-correct, and offers "reject" as easily as "accept" where the law requires it.
  - الشريط مترجم، ويمكن استخدامه بلوحة المفاتيح، وصحيح الاتجاه في RTL، ويتيح "الرفض" بسهولة "القبول" حيث يشترط القانون ذلك.
- [ ] Privacy policy and cookie list per language, linked in the footer, dated, matching the trackers actually loaded.
  - سياسة الخصوصية وقائمة ملفات الارتباط بكل لغة، مرتبطة في التذييل ومؤرخة ومطابقة لأدوات التتبع المحمّلة فعلاً.
- [ ] Prefer privacy-friendly measurement where possible (server-side tagging, cookieless/aggregate analytics) and never put personal data in URLs or analytics events.
  - فضّل القياس الأقل جمعاً للبيانات حيث أمكن (الوسوم من الخادم، والتحليلات دون ملفات ارتباط أو المجمّعة)؛ ولا تضع بيانات شخصية في الروابط أو أحداث التحليلات أبداً.
- [ ] Third-party scripts audited: purpose, data collected, consent category, performance cost, and no back-button or history manipulation (§4).
  - تدقيق سكربتات الطرف الثالث: الغرض، والبيانات المجمّعة، وفئة الموافقة، وكلفة الأداء، وعدم التلاعب بزر الرجوع أو السجل (§4).

---

## 28. Page templates · قوالب الصفحات

Copy-paste skeletons that combine the head (§8), the answer-block pattern (§22.2) and structured data (§12). Replace every `…` with real content; delete any block you have no real data for.
هياكل جاهزة للنسخ تجمع وسوم الصفحة (§8) ونمط كتلة الإجابة (§22.2) والبيانات المنظمة (§12). استبدل كل `…` بمحتوى حقيقي، واحذف أي جزء ليس لديك بيانات حقيقية له.

### 28.1 Universal `<head>` (Arabic page shown) · وسوم `<head>` العامة (مثال صفحة عربية)

```html
<!doctype html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>عنوان الصفحة الفريد | العلامة</title>
  <meta name="description" content="وصف فريد للصفحة يشرح القيمة ويدعو لإجراء.">
  <link rel="canonical" href="https://example.com/ar/page">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <link rel="alternate" hreflang="ar" href="https://example.com/ar/page">
  <link rel="alternate" hreflang="en" href="https://example.com/en/page">
  <link rel="alternate" hreflang="x-default" href="https://example.com/ar/page">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="العلامة">
  <meta property="og:title" content="عنوان الصفحة الفريد">
  <meta property="og:description" content="وصف فريد للصفحة.">
  <meta property="og:url" content="https://example.com/ar/page">
  <meta property="og:image" content="https://example.com/og/page-ar.jpg">
  <meta property="og:locale" content="ar_AR">
  <meta property="og:locale:alternate" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preload" as="image" href="/img/hero.avif" fetchpriority="high">
  <link rel="alternate" type="application/rss+xml" title="العلامة — المدونة" href="https://example.com/ar/feed.xml">
  <script type="application/ld+json">{ "@context": "https://schema.org", "@graph": [ … ] }</script>
</head>
```

### 28.2 Article with answer blocks · مقالة بنمط كتلة الإجابة

```html
<main>
  <nav aria-label="breadcrumb">…</nav>
  <article>
    <header>
      <h1>The main question or topic, phrased as people search it</h1>
      <p>By <a href="/en/authors/jane-doe" rel="author">Jane Doe</a>, role and credentials ·
         Published <time datetime="2026-11-05">5 Nov 2026</time> ·
         Updated <time datetime="2026-11-20">20 Nov 2026</time></p>
    </header>
    <aside aria-label="Key takeaways"><ul><li>…</li><li>…</li><li>…</li></ul></aside>
    <nav aria-label="Table of contents">…</nav>

    <section>
      <h2>What is X?</h2>
      <p><strong>X is …</strong> (a self-contained 40–60 word answer that makes sense when quoted alone).</p>
      <p>Supporting detail, example, and a cited source: <a href="https://primary-source.example">Source, 2026</a>.</p>
    </section>

    <section>
      <h2>How do you do X?</h2>
      <p>One-sentence summary of the process.</p>
      <ol><li>Verb-first step…</li><li>…</li><li>…</li></ol>
    </section>

    <section>
      <h2>X vs Y: which should you choose?</h2>
      <p>One-line verdict.</p>
      <table><thead><tr><th>Criterion</th><th>X</th><th>Y</th></tr></thead><tbody>…</tbody></table>
    </section>

    <section><h2>Frequently asked questions</h2>…</section>
    <footer>Author bio · sources · related articles (3–5 internal links)</footer>
  </article>
</main>
```

```json
{"@context":"https://schema.org","@graph":[
 {"@type":"BlogPosting","@id":"https://example.com/en/blog/x#article","headline":"…","description":"…",
  "inLanguage":"en","datePublished":"2026-11-05","dateModified":"2026-11-20",
  "author":{"@id":"https://example.com/en/authors/jane-doe#person"},
  "publisher":{"@id":"https://example.com/#org"},"image":["https://example.com/img/x-1200.jpg"],
  "mainEntityOfPage":{"@id":"https://example.com/en/blog/x#webpage"},
  "about":[{"@type":"Thing","name":"…","sameAs":"https://www.wikidata.org/wiki/Q…"}],
  "citation":["https://primary-source.example"]},
 {"@type":"Person","@id":"https://example.com/en/authors/jane-doe#person","name":"Jane Doe","jobTitle":"…",
  "url":"https://example.com/en/authors/jane-doe","sameAs":["https://www.linkedin.com/in/…"]}
]}
```

The `#webpage` and `#org` `@id`s must resolve to the site-wide WebPage and Organization nodes emitted on the same page (§12).
معرّفات `#webpage` و`#org` يجب أن تشير إلى عقدتي WebPage وOrganization العامتين المضمّنتين في الصفحة نفسها (§12).

### 28.3 "Facts about the brand" page · صفحة "حقائق عن العلامة"

Sections (in this order, every language): what it is (one paragraph) · founded / founders / HQ · products and services (one line each, linked) · pricing model · key numbers with dates and sources · awards/certifications (real only) · official profiles · press contact · "last updated".
الأقسام (بهذا الترتيب، بكل لغة): ما هي العلامة (فقرة واحدة) · سنة التأسيس / المؤسسون / المقر · المنتجات والخدمات (سطر لكل منها مع رابط) · نموذج التسعير · الأرقام الأساسية بتواريخها ومصادرها · الجوائز/الشهادات (الحقيقية فقط) · الحسابات الرسمية · التواصل الإعلامي · "آخر تحديث".

```json
{"@context":"https://schema.org","@graph":[
 {"@type":"AboutPage","@id":"https://example.com/en/facts#webpage","url":"https://example.com/en/facts",
  "name":"Facts about Brand","inLanguage":"en","dateModified":"2026-11-20","mainEntity":{"@id":"https://example.com/#org"}},
 {"@type":"Organization","@id":"https://example.com/#org","name":"Brand","alternateName":"العلامة",
  "url":"https://example.com/","logo":"https://example.com/logo.png","foundingDate":"2020",
  "founder":[{"@type":"Person","name":"…"}],"address":{"@type":"PostalAddress","addressLocality":"…","addressCountry":"SA"},
  "sameAs":["https://www.linkedin.com/company/…","https://x.com/…","https://www.wikidata.org/wiki/Q…"]}
]}
```

### 28.4 Glossary term · مصطلح في المسرد

```html
<article>
  <h1>What is X?</h1>  <!-- the Arabic page uses <h1>ما هو X؟</h1> -->
  <p><strong>X is …</strong> (1–2 sentence definition first).</p>
  <h2>Example</h2><p>…</p>
  <h2>Related terms</h2><ul><li><a href="/en/glossary/y">Y</a></li></ul>
</article>
```

```json
{"@context":"https://schema.org","@type":"DefinedTerm","@id":"https://example.com/en/glossary/x#term",
 "name":"X","description":"X is …","url":"https://example.com/en/glossary/x",
 "inDefinedTermSet":{"@type":"DefinedTermSet","@id":"https://example.com/en/glossary#set","name":"Brand glossary","inLanguage":"en"}}
```

### 28.5 Service / feature page · صفحة خدمة أو ميزة

Order: H1 (service + outcome) → 40–60 word answer to "what is it / who is it for" → problem → 3–5 step process → outcomes with real numbers → case study/testimonial → pricing or pricing model → FAQ from real questions → CTA + contact.
الترتيب: H1 (الخدمة + النتيجة) ← إجابة من 40–60 كلمة عن "ما هي ولمن" ← المشكلة ← عملية من 3–5 خطوات ← نتائج بأرقام حقيقية ← دراسة حالة/شهادة ← السعر أو نموذج التسعير ← أسئلة شائعة حقيقية ← دعوة لإجراء + تواصل.

```json
{"@context":"https://schema.org","@type":"Service","@id":"https://example.com/en/services/x#service",
 "name":"…","description":"…","provider":{"@id":"https://example.com/#org"},"areaServed":[{"@type":"Country","name":"Saudi Arabia"},{"@type":"Country","name":"United Arab Emirates"}],
 "offers":{"@type":"Offer","price":"499.00","priceCurrency":"USD","url":"https://example.com/en/services/x"}}
```

### 28.6 Comparison page · صفحة مقارنة

Order: verdict in one paragraph → criteria and methodology → comparison table → each option (pros, cons, best for, price "as of" date) → "Choose A if… / Choose B if…" → disclosure that one product is yours → last updated.
الترتيب: الحكم في فقرة ← المعايير والمنهجية ← جدول المقارنة ← كل خيار (الإيجابيات، السلبيات، الأنسب لـ، السعر بتاريخه) ← "اختر A إذا… / اختر B إذا…" ← الإفصاح أن أحد المنتجات منتجك ← آخر تحديث.

```json
{"@context":"https://schema.org","@type":"ItemList","name":"Best X tools in 2026","numberOfItems":3,
 "itemListOrder":"https://schema.org/ItemListOrderDescending",
 "itemListElement":[{"@type":"ListItem","position":1,"name":"…","url":"https://example.com/en/compare/x#a"}]}
```

`numberOfItems` must equal the real number of `ListItem` entries (one is shown for brevity).
قيمة `numberOfItems` يجب أن تساوي عدد عناصر `ListItem` الفعلي (عُرض عنصر واحد للاختصار).

### 28.7 Tool / calculator page · صفحة أداة أو حاسبة

Order: H1 + one-line purpose → working tool above the fold (no login wall for the basic result) → "how to use" in ≤ 3 steps → how it works / methodology → interpreting results → FAQ → related tools.
الترتيب: H1 + سطر يشرح الغرض ← أداة تعمل أعلى الصفحة (بلا اشتراط تسجيل دخول للنتيجة الأساسية) ← طريقة الاستخدام في ≤ 3 خطوات ← كيف تعمل / المنهجية ← تفسير النتائج ← أسئلة شائعة ← أدوات ذات صلة.

```json
{"@context":"https://schema.org","@type":"WebApplication","name":"…","url":"https://example.com/en/tools/x",
 "applicationCategory":"BusinessApplication","operatingSystem":"Any","browserRequirements":"Requires JavaScript",
 "offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"inLanguage":"en"}
```

---

## 29. Framework recipes · وصفات حسب إطار العمل

Use the project's existing tools first; add a package only if the project's rules allow new dependencies. Every recipe must end with the tests in §30.
استخدم أدوات المشروع الموجودة أولاً؛ ولا تضف حزمة إلا إذا سمحت قواعد المشروع بإضافة اعتماديات جديدة. وكل وصفة تنتهي باختبارات §30.

### 29.1 Laravel / Blade · Laravel / Blade
- [ ] One SEO service (or view component) builds a page DTO: title, description, canonical, robots, alternates, OG, breadcrumbs, JSON-LD graph; controllers pass page data, the layout renders `@include('seo-head')` once.
  - خدمة SEO واحدة (أو مكوّن عرض) تبني كائن بيانات للصفحة: العنوان، والوصف، وcanonical، وrobots، والبدائل، وOG، ومسار التنقّل، ومخطط JSON-LD؛ والمتحكمات تمرر البيانات، والقالب الرئيسي يعرضها مرة واحدة.
- [ ] Output JSON-LD with `{!! json_encode($graph, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG) !!}` (keeps Arabic readable and prevents `</script>` injection).
  - أخرج JSON-LD عبر `json_encode` بهذه الخيارات (تبقي العربية مقروءة وتمنع حقن `</script>`).
- [ ] `robots.txt`, `sitemap.xml` (index + pages), `llms.txt` as routes/controllers generated from models and named routes; cache them and clear the cache on content change (model observer), which also queues IndexNow.
  - `robots.txt` و`sitemap.xml` (فهرس + صفحات) و`llms.txt` كمسارات ومتحكمات تُولَّد من النماذج والمسارات المسمّاة؛ مع تخزين مؤقت يُمسح عند تغيّر المحتوى (Observer) ويضيف مهمة IndexNow في الطابور.
- [ ] Middleware: locale from URL prefix, `X-Robots-Tag` on non-indexable responses, security headers, HTTPS/host redirect.
  - Middleware: اللغة من بادئة الرابط، و`X-Robots-Tag` للاستجابات غير القابلة للفهرسة، وترويسات الأمان، وتحويل HTTPS والنطاق.
- [ ] Optional packages (only with approval): `spatie/laravel-sitemap`, `artesaos/seotools` or `ralphjsmit/laravel-seo`.
  - حزم اختيارية (بموافقة فقط): `spatie/laravel-sitemap` أو `artesaos/seotools` أو `ralphjsmit/laravel-seo`.
- [ ] Feature tests per locale: `$this->get('/ar/page')->assertOk()->assertSee('<link rel="canonical" href="…">', false)`; parse JSON-LD and assert types; assert sitemap and robots content.
  - اختبارات Feature لكل لغة: تحقق من الحالة وcanonical، وحلّل JSON-LD وتحقق من الأنواع، وتحقق من محتوى خريطة الموقع وrobots.

### 29.2 Next.js (App Router) · Next.js (App Router)
- [ ] `metadataBase` in the root layout; `generateMetadata()` (or the static `metadata` export) per route returns `title`, `description`, `alternates: { canonical, languages: { ar: '/ar/…', en: '/en/…', 'x-default': '/ar/…' } }` (`x-default` is accepted by the type; verify the output), `openGraph`, `twitter`, `robots`.
  - `metadataBase` في القالب الجذري؛ و`generateMetadata()` (أو تصدير `metadata` الثابت) لكل مسار تعيد العنوان والوصف و`alternates` (canonical واللغات و`x-default`) و`openGraph` و`twitter` و`robots`.
- [ ] Metadata streaming: since Next.js 15.2, dynamic `generateMetadata` may be streamed into `<body>` for JS-capable bots. Prefer static `metadata` or prerendered routes so tags land in the initial `<head>`; set `htmlLimitedBots` if every crawler must get head-blocking metadata, and verify with `curl`. [H]
  - بث البيانات الوصفية: منذ Next.js 15.2 قد يُبثّ `generateMetadata` الديناميكي داخل `<body>` للزواحف التي تنفّذ JS. فضّل تصدير `metadata` الثابت أو المسارات المعروضة مسبقاً لتظهر الوسوم في `<head>` الأولي؛ واضبط `htmlLimitedBots` إن احتجت الوسوم في `<head>` لكل الزواحف، وتحقق بـ `curl`. [H]
- [ ] `<html lang={locale} dir={dir}>` set in `app/[locale]/layout.tsx` from the route param.
  - ضبط `<html lang dir>` في `app/[locale]/layout.tsx` من معامل المسار.
- [ ] `app/sitemap.ts` (and `generateSitemaps()` above 50k URLs) and `app/robots.ts` generated from real data.
  - `app/sitemap.ts` (و`generateSitemaps()` فوق 50 ألف رابط) و`app/robots.ts` تُولَّد من البيانات الحقيقية.
- [ ] JSON-LD in a server component: `<script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(data).replace(/</g, '\\u003c') }} />`.
  - JSON-LD داخل مكوّن خادم مع استبدال `<` لمنع الحقن.
- [ ] Public pages are Server Components / SSG / ISR — never `'use client'` for primary content; check `curl` output.
  - الصفحات العامة مكوّنات خادم أو SSG أو ISR — لا `'use client'` للمحتوى الأساسي؛ وتحقق بـ `curl`.

### 29.3 Nuxt · Nuxt
- [ ] `useSeoMeta()` for title/description/OG/Twitter and `useHead({ htmlAttrs: { lang, dir } })` per page.
  - `useSeoMeta()` للعنوان والوصف وOG وTwitter، و`useHead({ htmlAttrs: { lang, dir } })` لكل صفحة.
- [ ] `@nuxtjs/i18n` with `useLocaleHead({ seo: true })` (set `i18n.baseUrl`) for hreflang, canonical and `og:locale`; `lang`/`dir` on by default; prefix strategy (`/ar/`, `/en/`).
  - `@nuxtjs/i18n` مع `useLocaleHead({ seo: true })` (واضبط `i18n.baseUrl`) لـ hreflang وcanonical و`og:locale`؛ و`lang`/`dir` مفعّلة افتراضياً؛ واستراتيجية البادئة (`/ar/`، `/en/`).
- [ ] Nuxt SEO modules (sitemap, robots, schema-org, og-image) or equivalent server routes; `routeRules` to prerender/SSR public pages.
  - وحدات Nuxt SEO (خريطة الموقع، robots، schema-org، صور OG) أو مسارات خادم مكافئة؛ و`routeRules` لعرض الصفحات العامة مسبقاً أو من الخادم.

### 29.4 WordPress · WordPress
- [ ] Exactly one SEO plugin (Yoast, Rank Math, SEOPress or AIOSEO) — disable overlapping schema/OG output from the theme or other plugins. [H]
  - إضافة SEO واحدة فقط (Yoast أو Rank Math أو SEOPress أو AIOSEO) — وعطّل أي مخطط أو OG مكرر من القالب أو إضافات أخرى. [H]
- [ ] Multilingual with WPML, Polylang or TranslatePress (they output hreflang); theme uses `language_attributes()` and RTL stylesheets.
  - تعدد اللغات عبر WPML أو Polylang أو TranslatePress (تُخرج hreflang)؛ والقالب يستخدم `language_attributes()` وأنماط RTL.
- [ ] Permalinks `/%postname%/`; attachment pages off (default on new installs since WP 6.4; on older sites disable via the SEO plugin or the `wp_attachment_pages_enabled` option); thin tag, date and author archives `noindex` or consolidated.
  - الروابط الدائمة `/%postname%/`؛ وصفحات المرفقات معطّلة (افتراضياً في التثبيتات الجديدة منذ WordPress 6.4؛ وفي المواقع الأقدم عبر إضافة SEO أو الخيار `wp_attachment_pages_enabled`)؛ وأرشيفات الوسوم والتواريخ والكتّاب الضعيفة `noindex` أو مدمجة.
- [ ] Caching + image optimization plugin, and audit every plugin's front-end scripts (performance and consent, §27).
  - إضافة تخزين مؤقت وتحسين صور، وتدقيق سكربتات كل إضافة في الواجهة (الأداء والموافقة، §27).

### 29.5 Astro, SvelteKit, React Router / Remix · Astro وSvelteKit وReact Router / Remix
- [ ] Astro: `site` in config, i18n routing, `@astrojs/sitemap` with the `i18n` option, a shared `<SEOHead>` component; static output by default.
  - Astro: ضبط `site`، وتوجيه i18n، و`@astrojs/sitemap` مع خيار `i18n`، ومكوّن `<SEOHead>` مشترك؛ والإخراج الثابت افتراضياً.
- [ ] SvelteKit: `<svelte:head>` per page, `prerender = true` for static pages, `+server.ts` endpoints for sitemap/robots.
  - SvelteKit: `<svelte:head>` لكل صفحة، و`prerender = true` للصفحات الثابتة، ونقاط `+server.ts` لخريطة الموقع وrobots.
- [ ] React Router v7 / Remix: route `meta` exports + loader data, server rendering on, resource routes for sitemap/robots.
  - React Router v7 / Remix: تصدير `meta` لكل مسار مع بيانات loader، وتفعيل العرض من الخادم، ومسارات موارد لخريطة الموقع وrobots.

### 29.6 Client-only SPA (CRA, Vite React/Vue/Angular) · تطبيق صفحة واحدة يعمل في المتصفح فقط
- [ ] [C] Move public pages to an SSR/SSG framework (Next, Nuxt, Astro, Angular SSR) or prerender them at build time; keep CSR only behind login.
  - [C] انقل الصفحات العامة إلى إطار SSR/SSG (Next أو Nuxt أو Astro أو Angular SSR) أو اعرضها مسبقاً وقت البناء؛ وأبقِ العرض في المتصفح خلف تسجيل الدخول فقط.
- [ ] Until then: prerendered HTML per route with real title/meta/canonical/JSON-LD, real 404 status for unknown routes, and a generated sitemap.
  - حتى يتم ذلك: HTML معروض مسبقاً لكل مسار بعنوان ووصف وcanonical وJSON-LD حقيقية، وحالة 404 حقيقية للمسارات غير الموجودة، وخريطة موقع مولّدة.

### 29.7 Static sites & other stacks · المواقع الثابتة وغيرها
- [ ] Generate head tags, sitemap, robots and llms.txt at build time from one data source (front matter / content collection); run the §30 crawl in CI after every build.
  - ولّد وسوم الصفحة وخريطة الموقع وrobots وllms.txt وقت البناء من مصدر بيانات واحد؛ وشغّل فحص §30 في CI بعد كل بناء.

---

## 30. Verification kit · أدوات التحقق

Nothing counts as done until it is verified. Use the table to verify each section, the commands for quick manual checks, and the crawl script for the whole site (locally, on staging and in CI).
لا يُعتبر أي بند منجزاً حتى يُتحقق منه. استخدم الجدول للتحقق من كل قسم، والأوامر للفحص اليدوي السريع، وسكربت الفحص للموقع كاملاً (محلياً وعلى بيئة التجربة وفي CI).

### 30.1 How to verify each section · كيف تتحقق من كل قسم

| § | Check · الفحص | Pass when · ينجح عندما |
|---|---|---|
| 1, 1.1 | `curl` robots.txt; test bot user agents; server logs<br>جلب robots.txt واختبار وكلاء البوتات والسجلات | 200, sitemap declared, private paths disallowed in every group, bots not blocked by WAF<br>يعيد 200، وخريطة الموقع معلنة، والمسارات الخاصة محظورة في كل مجموعة، والبوتات غير محجوبة |
| 2 | Crawl script; `curl -sI` on variants (http, www, trailing slash, params)<br>سكربت الفحص و`curl -sI` على صيغ الروابط | One self canonical per page; every variant = one 301 hop; unknown URL = 404<br>canonical ذاتي واحد؛ كل صيغة = تحويل واحد؛ الرابط غير الموجود = 404 |
| 3 | `curl -s URL` (no JS) and compare with the rendered DOM<br>جلب الصفحة دون JS ومقارنتها بالصفحة المعروضة | Title, meta, canonical, hreflang, JSON-LD and main text all present in raw HTML<br>كل العناصر والنص الأساسي موجودة في HTML الخام |
| 4 | `curl -sI` headers; SSL Labs / securityheaders-type scan<br>فحص الترويسات والشهادة | HTTPS only, HSTS, CSP, nosniff, Referrer-Policy, no version disclosure<br>HTTPS فقط مع كل الترويسات وبلا كشف للإصدار |
| 6, 7 | Lighthouse (lab), CrUX / Search Console CWV (field), devices at 375/768/1366/1920<br>Lighthouse وبيانات CrUX الميدانية والأجهزة | p75 LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1; no horizontal scroll<br>المؤشرات ضمن الحدود ولا تمرير أفقي |
| 8, 11 | Crawl script; spot-check templates<br>سكربت الفحص ومراجعة القوالب | No [C]/[H] issues; unique titles/descriptions; one H1; alt + dimensions<br>لا مشكلات حرجة أو عالية؛ عناوين وأوصاف فريدة؛ H1 واحد؛ نص بديل وأبعاد |
| 9 | `xmllint --noout`; crawl script on every sitemap URL<br>التحقق من XML وفحص كل روابط الخريطة | Valid XML, limits respected, every URL 200 + indexable + canonical<br>XML صالح وكل رابط 200 وقابل للفهرسة وcanonical |
| 10, 21 | Crawl script reciprocity check, per locale<br>فحص التبادلية لكل لغة | Self-reference, return links, one x-default, valid codes, `lang`/`dir` correct<br>إشارة ذاتية وروابط عودة وx-default واحد ورموز صحيحة |
| 12 | Crawl script + Rich Results Test + validator.schema.org<br>السكربت وأداتا التحقق من المخطط | Valid JSON, no retired rich-result types relied on, data matches the visible page<br>JSON صالح ولا يعتمد على أنواع أُوقفت نتائجها، ومطابق للصفحة |
| 13, 22 | Manual review of top pages against §22.2; facts page exists<br>مراجعة يدوية لأهم الصفحات | Answer-first blocks, sources, author + dates, facts page live<br>إجابة أولاً ومصادر وكاتب وتواريخ وصفحة الحقائق منشورة |
| 17 | Lighthouse accessibility (+ agentic category if available); keyboard test<br>Lighthouse لإمكانية الوصول واختبار لوحة المفاتيح | Accessibility audits pass; all actions reachable by keyboard<br>اجتياز فحوص الوصول والوصول لكل إجراء بلوحة المفاتيح |
| 24 | Share-of-voice prompt run<br>تشغيل أسئلة نسبة الظهور | Baseline recorded; errors turned into tasks<br>خط أساس مسجّل والأخطاء تحولت لمهام |
| 25 | Redirect-map test on 100+ old URLs<br>اختبار خريطة التحويل | 100% single 301 to the right page<br>كل الروابط تحويل واحد للصفحة الصحيحة |
| 27 | Load page with consent rejected; check network tab<br>تحميل الصفحة مع رفض الموافقة | No non-essential trackers fire; CLS unaffected<br>لا تعمل أدوات التتبع غير الضرورية ولا يتأثر CLS |

### 30.2 Quick commands · أوامر سريعة

```bash
# HTTPS + host: expect one 301 to the canonical https host
curl -sI http://example.com/ | grep -iE '^(HTTP|location)'
curl -sI https://www.example.com/ | grep -iE '^(HTTP|location)'

# Security headers and version disclosure
curl -sI https://example.com/ | grep -iE 'strict-transport|content-security|x-content-type|referrer-policy|x-powered-by|^server'

# robots.txt and sitemap validity
curl -s https://example.com/robots.txt
curl -s https://example.com/sitemap.xml | xmllint --noout - && echo "sitemap XML valid"   # Debian/Ubuntu: apt install libxml2-utils

# Essentials present in raw HTML (no JavaScript)
curl -s https://example.com/ar/page | grep -oE '<title>[^<]*|rel="canonical"[^>]*|hreflang="[^"]*"|application/ld\+json' | head -20

# Real 404 for unknown URLs (must print 404)
curl -s -o /dev/null -w '%{http_code}\n' https://example.com/this-page-should-not-exist-9271

# Spoofed UAs: a 403 is NORMAL for Googlebot/bingbot (WAFs verify bot IPs). Confirm real-bot access in server logs,
# Search Console Crawl Stats and Bing URL Inspection (§32.3); a 403 for AI-search UAs may still need a WAF rule review.
for ua in Googlebot bingbot OAI-SearchBot Claude-SearchBot PerplexityBot Applebot; do
  printf '%-18s' "$ua"; curl -s -o /dev/null -w '%{http_code}\n' -A "Mozilla/5.0 (compatible; $ua)" https://example.com/
done

# Lighthouse (lab data)
npx lighthouse https://example.com/ar --only-categories=performance,seo,accessibility,best-practices \
  --output=json --output-path=./lighthouse-ar.json --quiet --chrome-flags="--headless"
```

### 30.3 Whole-site crawl script · سكربت فحص الموقع كاملاً

Save as `seo_audit.py` (Python 3.9+, standard library only). It reads every sitemap (including sitemap indexes) and checks status, title, description, H1, canonical, hreflang self/x-default/return links, `lang`/`dir`, JSON-LD validity and deprecated types, OG/Twitter, images, HTML size and duplicates. It exits with code 1 when any Critical issue exists, so it can gate CI.
احفظه باسم `seo_audit.py` (Python 3.9 أو أحدث، دون مكتبات خارجية). يقرأ كل خرائط الموقع (بما فيها الفهارس) ويفحص الحالة والعنوان والوصف وH1 وcanonical وhreflang (الإشارة الذاتية وx-default وروابط العودة) و`lang`/`dir` وصلاحية JSON-LD والأنواع الملغاة وOG/Twitter والصور وحجم HTML والتكرار. ويخرج بالرمز 1 عند وجود أي مشكلة حرجة، فيصلح كبوابة في CI.

```bash
python3 seo_audit.py https://example.com/sitemap.xml
python3 seo_audit.py https://example.com/sitemap.xml --map https://example.com=https://staging.example.com --insecure --json report.json
```

```python
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
```

### 30.4 Lighthouse CI budgets · ميزانيات Lighthouse في CI

`lighthouserc.json` (lab proxies: TBT stands in for INP, which needs real users):
ملف `lighthouserc.json` (مقاييس مختبرية: TBT بديل تقريبي لـ INP الذي يحتاج مستخدمين حقيقيين):

```json
{
  "ci": {
    "collect": { "url": ["https://staging.example.com/ar", "https://staging.example.com/en"], "numberOfRuns": 3 },
    "assert": {
      "aggregationMethod": "median-run",
      "assertions": {
        "categories:seo": ["error", { "minScore": 0.95 }],
        "categories:accessibility": ["error", { "minScore": 0.9 }],
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }],
        "total-blocking-time": ["warn", { "maxNumericValue": 200 }]
      }
    }
  }
}
```

---

## 31. Scoring · نظام الدرجات

Score after every audit and after every major release; store the scores with the date so progress is visible.
احسب الدرجات بعد كل تدقيق وكل إصدار كبير؛ واحفظها مع التاريخ ليظهر التقدم.

### 31.1 How an item counts · كيف يُحسب البند
- Item weights: [C] 10 · [H] 5 · [M] 2 · [L] 1 · untagged 2 · [I] 0. Items marked "n.a." are excluded.
  - أوزان البنود: [C] 10 · [H] 5 · [M] 2 · [L] 1 · غير موسوم 2 · [I] 0. والبنود "لا ينطبق" مستبعدة.
- Category score = 100 × (weights of passed items ÷ weights of applicable items). Any failed [C] caps its category at 50.
  - درجة الفئة = 100 × (أوزان البنود الناجحة ÷ أوزان البنود المنطبقة). وأي بند [C] فاشل يجعل سقف فئته 50.
- Bands: 90–100 excellent · 70–89 good · 50–69 needs work · < 50 critical.
  - المستويات: 90–100 ممتاز · 70–89 جيد · 50–69 يحتاج عملاً · أقل من 50 حرج.

### 31.2 SEO Health Score (100) · درجة صحة SEO

| Category · الفئة | Weight · الوزن | Sections · الأقسام |
|---|---|---|
| Technical · تقني | 22% | §1, §2, §4, §5, §9, §10, §21 |
| Content quality · جودة المحتوى | 23% | §13, §14, §20.3 |
| On-page · عناصر الصفحة | 20% | §8, §20.2, §21.3 |
| Structured data · البيانات المنظمة | 10% | §12, §15/§16 when applicable |
| Performance · الأداء | 10% | §6, §7, §20.6 |
| AI search readiness · جاهزية بحث الذكاء الاصطناعي | 10% | §1.1, §3, §17 |
| Images · الصور | 5% | §11 |

### 31.3 AEO Score (100) · درجة AEO

| Category · الفئة | Points · النقاط | Sections · الأقسام |
|---|---|---|
| Access & rendering · الوصول والعرض | 15 | §1.1, §3, §24.2 |
| Question coverage · تغطية الأسئلة | 15 | §22.1 (share of bank questions with a mapped, published answer) |
| Answer format · شكل الإجابة | 15 | §22.2 |
| Evidence & citability · الأدلة وقابلية الاقتباس | 15 | §22.3, §13.3 |
| Entity clarity · وضوح الكيان | 15 | §22.4, §23.1 |
| Off-site presence · الحضور خارج الموقع | 15 | §23.2, §23.3 |
| Measured share of voice · نسبة الظهور المقاسة | 10 | §24.3: 0 = not measured · 5 = measured monthly · 10 = measured and rising for 3 months or ≥ the top competitor |

### 31.4 Score report format · صيغة تقرير الدرجات

| Date | SEO | AEO | Lowest category · أضعف فئة | Open [C] | Open [H] | Next 90-day focus · تركيز التسعين يوماً |
|---|---|---|---|---|---|---|
| YYYY-MM-DD | 0–100 | 0–100 | … | n | n | … |

---

## 32. Operations & governance · التشغيل والحوكمة

### 32.1 CI/CD gates · بوابات CI/CD
- [ ] On every pull request: SEO feature tests (§0.7) + the crawl script (§30.3) against the preview/staging build; fail on any [C]. [H]
  - في كل طلب دمج: اختبارات SEO (§0.7) وسكربت الفحص (§30.3) على نسخة المعاينة أو التجربة؛ والفشل عند أي [C]. [H]
- [ ] Lighthouse CI budgets (§30.4) on the top templates.
  - ميزانيات Lighthouse CI (§30.4) على أهم القوالب.
- [ ] Drift check (§18) against the stored baseline; CRITICAL drift blocks the release unless explicitly approved.
  - فحص الانحراف (§18) مقابل خط الأساس المحفوظ؛ والانحراف الحرج يوقف الإصدار ما لم تتم الموافقة عليه صراحة.
- [ ] A guard test that production never serves `Disallow: /`, a site-wide `noindex`, or staging hostnames in canonicals/sitemaps. [C]
  - اختبار حماية يضمن ألا تقدّم بيئة الإنتاج أبداً `Disallow: /` أو `noindex` شاملاً أو نطاقات التجربة في canonical أو خريطة الموقع. [C]

### 32.2 Review cadence · جدول المراجعة

| Frequency · التكرار | Tasks · المهام |
|---|---|
| Weekly · أسبوعياً | Search Console + Bing errors and coverage, new 404/5xx, crawl anomalies, new content passes §28 templates<br>أخطاء وتغطية Search Console وBing، وأخطاء 404/5xx الجديدة، وشذوذ الزحف، ومطابقة المحتوى الجديد للقوالب |
| Monthly · شهرياً | Full crawl (§30.3), CWV field data, AI share-of-voice run (§24.3), unlinked mentions (§23.2), indexed vs intended count, content-decay list<br>فحص كامل، وبيانات CWV الميدانية، واختبار نسبة الظهور، والإشارات بلا رابط، والمفهرس مقابل المستهدف، وقائمة المحتوى المتراجع |
| Quarterly · كل ربع سنة | Re-verify volatile facts (§34), refresh top answer pages, schema validation, robots/AI-crawler policy review, competitor and SERP review, scores (§31)<br>إعادة التحقق من الحقائق المتغيرة، وتحديث أهم صفحات الإجابة، والتحقق من المخطط، ومراجعة سياسة الزواحف، ومراجعة المنافسين، والدرجات |
| Yearly · سنوياً | Full audit, information architecture and cluster review, prune/merge old content, strategy and KPI reset<br>تدقيق كامل، ومراجعة البنية والمجموعات، ودمج أو حذف المحتوى القديم، وتحديث الاستراتيجية والمؤشرات |

### 32.3 Server log analysis · تحليل سجلات الخادم
- [ ] Keep access logs ≥ 90 days with user agent, status, response time and URL.
  - احتفظ بسجلات الوصول 90 يوماً على الأقل مع وكيل المستخدم والحالة وزمن الاستجابة والرابط.
- [ ] Verify real bots, not just user-agent strings: reverse DNS then forward DNS for Googlebot (`googlebot.com`/`google.com`) and Bingbot (`search.msn.com`), or the IP ranges vendors publish.
  - تحقق من البوتات الحقيقية لا من نص وكيل المستخدم فقط: DNS العكسي ثم الأمامي لـ Googlebot وBingbot، أو نطاقات IP التي تنشرها الجهات.
- [ ] Track: share of bot hits on important vs junk URLs (parameters, filters, redirects, 404s), status codes served to bots, 403/429 blocks, time from publish to first crawl.
  - تابع: نسبة زيارات البوتات للروابط المهمة مقابل غير المفيدة (المعاملات، الفلاتر، التحويلات، 404)، ورموز الحالة المقدّمة للبوتات، وحالات الحظر 403/429، والمدة من النشر حتى أول زحف.

### 32.4 Content decay & pruning · تراجع المحتوى والتنقية
- [ ] Pages losing > 30% of clicks year over year → refresh (facts, dates, answer blocks, internal links).
  - الصفحات التي تفقد أكثر من 30% من النقرات مقارنة بالفترة نفسها من العام السابق ← تحديث (الحقائق، التواريخ، كتل الإجابة، الروابط الداخلية).
- [ ] Pages with no traffic, links or purpose for 12+ months → improve, merge (301 to the best match) or remove (410); never mass-delete without a redirect review.
  - الصفحات بلا زيارات أو روابط أو غرض لمدة 12 شهراً فأكثر ← تحسين، أو دمج (301 لأنسب صفحة)، أو حذف (410)؛ ولا حذف جماعي دون مراجعة التحويلات.

### 32.5 Penalties, updates & recovery · العقوبات والتحديثات والتعافي
- [ ] Manual action (Search Console): fix every listed issue across the site, document the fixes, then file a reconsideration request. [C]
  - الإجراء اليدوي (Search Console): أصلح كل المشكلات المذكورة في كامل الموقع، ووثّق الإصلاحات، ثم قدّم طلب إعادة النظر. [C]
- [ ] Security issue / hacked content: clean, close the vulnerability, rotate credentials, then request a review. [C]
  - مشكلة أمنية أو محتوى مخترق: نظّف، وأغلق الثغرة، وغيّر بيانات الدخول، ثم اطلب المراجعة. [C]
- [ ] Algorithmic drop: match the date against the Google Search Status Dashboard; wait until a rollout finishes before changing things; compare winners and losers by template and intent; improve helpfulness and E-E-A-T — there is no reconsideration request, recovery usually shows after later updates.
  - تراجع خوارزمي: طابق التاريخ مع لوحة حالة بحث Google؛ وانتظر انتهاء التحديث قبل التغيير؛ وقارن الصفحات الرابحة والخاسرة حسب القالب والنية؛ وحسّن الفائدة وE-E-A-T — لا يوجد طلب إعادة نظر، والتعافي يظهر عادة بعد تحديثات لاحقة.

### 32.6 Ownership · المسؤوليات
- [ ] Named owners for SEO decisions, content, engineering and analytics; every open [C]/[H] has an owner and a due date.
  - مسؤولون محددون بالاسم لقرارات SEO والمحتوى والهندسة والتحليلات؛ ولكل بند [C]/[H] مفتوح مسؤول وموعد.

---

## 33. Bilingual glossary · مسرد المصطلحات

| Term | المصطلح | Meaning · المعنى |
|---|---|---|
| SEO | تحسين محركات البحث | Making pages discoverable, understandable and rankable · جعل الصفحات قابلة للاكتشاف والفهم والترتيب |
| AEO | تحسين محركات الإجابة | Making content the source answer engines quote · جعل المحتوى المصدر الذي تقتبسه محركات الإجابة |
| GEO / LLM SEO | تحسين الظهور في الذكاء الاصطناعي التوليدي | AEO focused on generative AI answers · AEO مع التركيز على إجابات الذكاء الاصطناعي التوليدي |
| SERP | صفحة نتائج البحث | The results page · صفحة النتائج |
| Crawling | الزحف | Bots fetching pages · جلب البوتات للصفحات |
| Indexing | الفهرسة | Storing pages for retrieval · حفظ الصفحات لاسترجاعها |
| Rendering | العرض | Building the final page, incl. JavaScript · بناء الصفحة النهائية بما فيها JavaScript |
| SSR / SSG / CSR | العرض من الخادم / التوليد الثابت / العرض في المتصفح | Where HTML is produced · مكان إنتاج HTML |
| Canonical | الرابط المعتمد (الأساسي) | The preferred URL of duplicate pages · الرابط المفضل بين الصفحات المكررة |
| Hreflang | hreflang | Links between language/region versions · الربط بين نسخ اللغات والمناطق |
| x-default | x-default | Fallback version for unmatched users · النسخة الاحتياطية لباقي المستخدمين |
| noindex | منع الفهرسة | Directive to keep a page out of the index · توجيه بإبقاء الصفحة خارج الفهرس |
| Sitemap | خريطة الموقع | XML list of indexable URLs · قائمة XML بالروابط القابلة للفهرسة |
| robots.txt | ملف robots | Crawl rules per user agent · قواعد الزحف لكل زاحف |
| llms.txt | ملف llms | Markdown map of key pages for LLMs · خريطة Markdown لأهم الصفحات للنماذج |
| IndexNow | IndexNow | Instant URL-change notification protocol · بروتوكول إشعار فوري بتغيّر الروابط |
| Structured data / JSON-LD | البيانات المنظمة | Machine-readable page facts (schema.org) · حقائق الصفحة بصيغة تقرؤها الآلة |
| Rich result | النتيجة المنسّقة | Enhanced SERP display from structured data · عرض محسّن في النتائج |
| Entity | الكيان | A uniquely identifiable thing (brand, person, concept) · شيء محدد الهوية (علامة، شخص، مفهوم) |
| `sameAs` | sameAs | Links connecting an entity to its profiles · روابط تربط الكيان بحساباته |
| E-E-A-T | التجربة والخبرة والموثوقية والجدارة بالثقة | Experience, expertise, authoritativeness, trust · معايير جودة المحتوى ومصدره |
| YMYL | مواضيع تمس المال والحياة | Topics affecting health, money, safety · مواضيع تؤثر في الصحة والمال والسلامة |
| Featured snippet | المقتطف المميز | Answer box at the top of results · مربع الإجابة أعلى النتائج |
| PAA | أسئلة ذات صلة | "People also ask" questions · أسئلة "يسأل الناس أيضاً" |
| AI Overviews / AI Mode | ملخصات الذكاء الاصطناعي / وضع الذكاء الاصطناعي | Google's generative answers · إجابات Google التوليدية |
| Share of voice | نسبة الظهور | % of answers mentioning the brand · نسبة الإجابات التي تذكر العلامة |
| Core Web Vitals (LCP, INP, CLS) | مؤشرات أداء الويب الأساسية | Loading, responsiveness, visual stability · التحميل والاستجابة والثبات البصري |
| TTFB | زمن أول بايت | Time to first byte from the server · زمن وصول أول بايت من الخادم |
| Crawl budget | ميزانية الزحف | How much a bot crawls a site · مقدار ما يزحفه البوت في الموقع |
| Orphan page | صفحة يتيمة | Page with no internal links to it · صفحة لا يشير إليها أي رابط داخلي |
| Cannibalization | التنافس الداخلي | Several pages targeting the same query · عدة صفحات تستهدف الاستعلام نفسه |
| Pillar / cluster | الصفحة المحورية / المجموعة | Hub page and its supporting pages · صفحة محور وصفحاتها الداعمة |
| Doorway page | صفحة المدخل | Near-duplicate page made only to rank · صفحة شبه مكررة لغرض الترتيب فقط |
| Soft 404 | خطأ 404 ضمني (soft 404) | Error page that returns 200 · صفحة خطأ تعيد 200 |
| 301 / 302 / 410 | تحويل دائم / مؤقت / محذوف نهائياً | Permanent / temporary redirect / gone · رموز التحويل والحذف |
| Anchor text | نص الرابط | Clickable text of a link · النص القابل للنقر في الرابط |
| Backlink | رابط خلفي | Link from another site · رابط من موقع آخر |
| NAP | الاسم والعنوان والهاتف | Name, address, phone · بيانات النشاط المحلي |
| SXO | تحسين تجربة البحث | Matching page type to search intent · مطابقة نوع الصفحة لنية البحث |
| RTL | من اليمين لليسار | Right-to-left scripts · الأنظمة الكتابية من اليمين لليسار |

---

## 34. Keeping this spec current · صيانة هذه المواصفة

**Last verified · آخر تحقق:** 2026-11 · **Version · الإصدار:** 1.2

### 34.1 Re-verify every quarter · أعد التحقق كل ربع سنة
- [ ] Core Web Vitals metrics and thresholds (§7).
  - مقاييس Core Web Vitals وحدودها (§7).
- [ ] Rich-result support and deprecated schema types (§12.2), merchant and local requirements (§15, §16).
  - دعم النتائج المنسّقة وأنواع المخطط الملغاة (§12.2)، ومتطلبات المتاجر والمحلي (§15، §16).
- [ ] Crawler user agents and what each controls (§1.1, §24.1).
  - وكلاء الزواحف وما يتحكم به كل منها (§1.1، §24.1).
- [ ] Google spam policies, AI-feature controls and snippet controls (§4, §13.4, §22.6).
  - سياسات Google لمكافحة السبام وضوابط ميزات الذكاء الاصطناعي والمقتطفات (§4، §13.4، §22.6).
- [ ] Agent standards: llms.txt, WebMCP, well-known files (§17).
  - معايير الوكلاء: llms.txt وWebMCP وملفات well-known (§17).
- [ ] Privacy laws per market (§27) and platform features for social search (§26.5).
  - قوانين الخصوصية لكل سوق (§27) ومزايا البحث في المنصات الاجتماعية (§26.5).

### 34.2 Official sources · المصادر الرسمية
Google Search Central (developers.google.com/search) · Google Search Status Dashboard (status.search.google.com) · web.dev (Core Web Vitals) · Bing Webmaster Tools and guidelines (bing.com/webmasters) · schema.org releases · IndexNow (indexnow.org) · the crawler documentation of OpenAI, Anthropic, Perplexity and Apple · W3C Internationalization (w3.org/International) · WCAG 2.2 (w3.org/WAI) · Lighthouse documentation. When sources conflict, the official documentation wins over blogs and third-party tools.
المصادر: Google Search Central، ولوحة حالة بحث Google، وweb.dev، وBing Webmaster Tools، وإصدارات schema.org، وIndexNow، وتوثيق زواحف OpenAI وAnthropic وPerplexity وApple، وW3C Internationalization، وWCAG 2.2، وتوثيق Lighthouse. وعند التعارض، المصدر الرسمي هو المرجع وليس المدونات أو أدوات الطرف الثالث.

### 34.3 Update rules · قواعد التحديث
- [ ] When a fact changes: update the item in **both** languages, update "Last verified", and add a changelog line. Mark third-party observations as *heuristic*.
  - عند تغيّر حقيقة: حدّث البند **باللغتين**، وحدّث "آخر تحقق"، وأضف سطراً لسجل التغييرات. وعلّم ملاحظات الأطراف الثالثة بأنها *إرشادية*.
- [ ] Never delete a requirement silently; mark it "retired (date, reason)" for one version, then remove it.
  - لا تحذف متطلباً بصمت؛ علّمه "مُلغى (التاريخ، السبب)" لإصدار واحد ثم احذفه.

### 34.4 Changelog · سجل التغييرات

| Version | Date | Change · التغيير |
|---|---|---|
| 1.0 | 2026-11 | Merged extended EN/AR spec + LLM optimization guide into one bilingual file · دمج المواصفة الموسّعة ودليل تحسين النماذج في ملف واحد ثنائي اللغة |
| 1.1 | 2026-11 | Added Start here, §23–§34 (definition of done renumbered): off-site authority, per-engine AEO, migrations, more search surfaces, privacy, templates, framework recipes, verification kit, scoring, operations, glossary, maintenance · إضافة "ابدأ من هنا" والأقسام 23–34 |
| 1.2 | 2026-11 | Public release: fact-check against primary sources (≈150 corrections), audit mode in §0, §35 site blueprint (pages, sections, files, head, HTTP, platform settings, audit report), §36 special cases, script fixes (gzip sitemaps, SVG titles, multi-value headers, charsets, RTL ranges, retired types as Low); definition of done → §37 · إصدار عام: تدقيق الحقائق، ووضع التدقيق، ومخطط الموقع §35، والحالات الخاصة §36، وإصلاحات السكربت |

---

## 35. Site blueprint: essential pages, sections, files & settings · مخطط الموقع: الصفحات والأقسام والملفات والإعدادات الأساسية

Use this section to audit **any** website (with or without its source code) and tell the owner exactly which pages, page sections, files and settings are missing, wrong or optional. Levels: **Required** (every public website) · **Recommended** (most websites) · **Conditional** (only for the stated site type).
استخدم هذا القسم لتدقيق **أي** موقع (بوجود الكود أو بدونه) وإخبار المالك بدقة بالصفحات وأقسام الصفحات والملفات والإعدادات الناقصة أو الخاطئة أو الاختيارية. المستويات: **إلزامي** (كل موقع عام) · **موصى به** (معظم المواقع) · **مشروط** (لنوع الموقع المذكور فقط).

### 35.1 Essential pages · الصفحات الأساسية

| Page · الصفحة | Level · المستوى | Index? · فهرسة؟ | Schema · المخطط | Must contain · يجب أن تحتوي |
|---|---|---|---|---|
| Home<br>الرئيسية | Required<br>إلزامي | Yes | `WebSite` + `Organization` + `WebPage` | Clear value proposition in the first screen, links to every main section, trust signals<br>قيمة واضحة في أول شاشة، وروابط لكل الأقسام الرئيسية، وإشارات ثقة |
| About<br>من نحن | Required<br>إلزامي | Yes | `AboutPage` | Who, why, team/founders, history, mission, real photos<br>من نحن، ولماذا، والفريق والمؤسسون، والتاريخ، والرسالة، وصور حقيقية |
| Contact<br>تواصل معنا | Required<br>إلزامي | Yes | `ContactPage` | Email, phone and/or form, address if any, response time, hours<br>البريد والهاتف و/أو النموذج، والعنوان إن وُجد، ووقت الرد، وساعات العمل |
| Privacy policy<br>سياسة الخصوصية | Required<br>إلزامي | Yes | `WebPage` | Data collected, purpose, rights, contact, date, per language<br>البيانات المجمّعة، والغرض، والحقوق، والتواصل، والتاريخ، بكل لغة |
| Terms of service<br>الشروط والأحكام | Required<br>إلزامي | Yes | `WebPage` | Usage terms, liability, governing law, date<br>شروط الاستخدام، والمسؤولية، والقانون الحاكم، والتاريخ |
| Custom 404 page<br>صفحة 404 مخصصة | Required<br>إلزامي | No (status 404) | — | Real 404 status, search box or main links, language-aware<br>حالة 404 حقيقية، ومربع بحث أو روابط رئيسية، وبلغة الزائر |
| Main service/product pages (one per offer)<br>صفحة لكل خدمة أو منتج رئيسي | Required<br>إلزامي | Yes | `Service` / `Product` / `SoftwareApplication` | §14.2 anatomy, §28.5 template<br>البنية في §14.2 والقالب في §28.5 |
| Cookie policy / preferences<br>سياسة ملفات الارتباط والتفضيلات | Conditional: cookies needing consent<br>مشروط: ملفات ارتباط تحتاج موافقة | Yes | `WebPage` | Cookie list matching real trackers, link to change preferences<br>قائمة مطابقة لأدوات التتبع الفعلية، ورابط لتغيير التفضيلات |
| FAQ / help center<br>الأسئلة الشائعة / مركز المساعدة | Recommended<br>موصى به | Yes | `WebPage` (FAQ content, §12.2) | Real customer questions, answer-first (§22.2)<br>أسئلة العملاء الحقيقية بنمط الإجابة أولاً |
| Facts about the brand<br>حقائق عن العلامة | Recommended (AEO)<br>موصى به (AEO) | Yes | `AboutPage` + `Organization` | §22.3, template §28.3<br>§22.3 والقالب §28.3 |
| Pricing<br>الأسعار | Recommended (SaaS, services)<br>موصى به | Yes | `Offer` / `WebPage` | Plans, what's included, currency, "as of" date, FAQ<br>الخطط، وما تشمله، والعملة، وتاريخ السعر، وأسئلة شائعة |
| Blog / articles hub<br>المدونة / مركز المقالات | Recommended<br>موصى به | Yes | `CollectionPage` + `ItemList` | Crawlable pagination, categories, latest posts<br>ترقيم قابل للزحف، وتصنيفات، وأحدث المقالات |
| Author pages<br>صفحات الكتّاب | Conditional: articles<br>مشروط: وجود مقالات | Yes | `ProfilePage` + `Person` | Photo, credentials, bio, `sameAs`, list of articles<br>صورة، ومؤهلات، ونبذة، و`sameAs`، وقائمة المقالات |
| Glossary<br>المسرد | Recommended (AEO)<br>موصى به (AEO) | Yes | `DefinedTermSet` / `DefinedTerm` | One URL per term, template §28.4<br>رابط لكل مصطلح، والقالب §28.4 |
| Case studies / testimonials<br>دراسات الحالة / الشهادات | Recommended<br>موصى به | Yes | `Article` / `Review` (real only) | Named clients (with permission), numbers, dates<br>عملاء بالاسم (بإذنهم)، وأرقام، وتواريخ |
| HTML sitemap<br>خريطة موقع HTML | Recommended (large sites)<br>موصى به (للمواقع الكبيرة) | Yes | `CollectionPage` | Links to every section and key page<br>روابط لكل قسم وأهم الصفحات |
| Press / media kit<br>الملف الصحفي | Recommended<br>موصى به | Yes | `WebPage` | §23.1<br>§23.1 |
| Careers<br>الوظائف | Conditional: hiring<br>مشروط: عند التوظيف | Yes | `JobPosting` per job | One URL per open role; remove or mark expired roles<br>رابط لكل وظيفة، وحذف المنتهية أو تعليمها |
| Accessibility statement<br>بيان إمكانية الوصول | Recommended (required in some jurisdictions)<br>موصى به (إلزامي في بعض الدول) | Yes | `WebPage` | Standard targeted (WCAG 2.2 AA), known gaps, contact<br>المعيار المستهدف، والقصور المعروف، والتواصل |
| Legal notice / imprint<br>البيانات القانونية للجهة | Conditional: e.g. Germany/Austria<br>مشروط: مثل ألمانيا والنمسا | Yes | `WebPage` | Legal entity, registration, address<br>الكيان القانوني، والسجل، والعنوان |
| Editorial & corrections policy<br>سياسة التحرير والتصحيح | Conditional: publishers, YMYL<br>مشروط: الناشرون ومواضيع YMYL | Yes | `WebPage` | How content is made, reviewed, corrected; AI use<br>كيف يُكتب المحتوى ويُراجع ويُصحح؛ واستخدام الذكاء الاصطناعي |
| Shipping, returns & refunds<br>الشحن والإرجاع والاسترداد | Conditional: e-commerce<br>مشروط: المتاجر | Yes | `MerchantReturnPolicy` (§16) | Countries, costs, windows, process<br>الدول، والتكاليف، والمدد، والإجراءات |
| Locations / store locator<br>الفروع / محدد المواقع | Conditional: local<br>مشروط: محلي | Yes | `LocalBusiness` subtype per location | §15<br>§15 |
| Docs, changelog, status, trust/security<br>التوثيق وسجل التغييرات والحالة والأمان | Conditional: SaaS / developer products<br>مشروط: SaaS ومنتجات المطورين | Yes (status: optional) | `TechArticle` / `WebPage` | Versioned docs, dated changelog, uptime history, compliance info<br>توثيق بالإصدارات، وسجل مؤرخ، وتاريخ التشغيل، ومعلومات الامتثال |
| Comparison / alternatives<br>المقارنات / البدائل | Conditional: competitive market<br>مشروط: سوق تنافسي | Yes | `ItemList` | §14.4, template §28.6<br>§14.4 والقالب §28.6 |
| Internal search results<br>نتائج البحث الداخلي | Conditional: site search<br>مشروط: وجود بحث داخلي | **No** (`noindex, follow`) | — | Never in the sitemap<br>لا تدخل خريطة الموقع أبداً |
| Login, account, cart, checkout, thank-you<br>الدخول والحساب والسلة والدفع والشكر | Conditional<br>مشروط | **No** (auth / `noindex`) | — | Protected by authentication, excluded from sitemap<br>محمية بتسجيل الدخول ومستبعدة من خريطة الموقع |
| Custom 5xx / maintenance page<br>صفحة خطأ الخادم / الصيانة | Recommended<br>موصى به | No (status 5xx / 503) | — | Maintenance returns `503` + `Retry-After`, never `200`<br>الصيانة تعيد `503` مع `Retry-After` وليس `200` |

### 35.2 Page anatomy (sections every page needs) · بنية الصفحة (الأقسام التي تحتاجها كل صفحة)

**Global header · الترويسة العامة**
- [ ] Skip-to-content link; logo linked to the home page of the current language with the brand as accessible name. [M]
  - رابط "تخطَّ إلى المحتوى"؛ وشعار يرتبط بالرئيسية في اللغة الحالية واسمه الوصولي اسم العلامة. [M]
- [ ] Primary navigation in `<nav>` with crawlable `<a href>` links to every main section (no JS-only menus, no hover-only menus). [H]
  - القائمة الرئيسية داخل `<nav>` بروابط `<a href>` قابلة للزحف لكل قسم رئيسي (لا قوائم تعمل بـ JS فقط أو بالتمرير فقط). [H]
- [ ] Language switcher linking to the equivalent page (§21.1); site search if the site has one; one primary CTA.
  - مبدّل لغة يرتبط بالصفحة المقابلة (§21.1)؛ وبحث داخلي إن وُجد؛ ودعوة رئيسية واحدة لإجراء.

**Content area · منطقة المحتوى**
- [ ] Breadcrumb (non-home pages) → one H1 → a 40–60-word answer or summary → body sections with H2/H3 → related links → CTA. [H]
  - مسار التنقّل (لغير الرئيسية) ← H1 واحد ← إجابة أو ملخص من 40–60 كلمة ← أقسام المتن بـ H2/H3 ← روابط ذات صلة ← دعوة لإجراء. [H]
- [ ] Articles add: author box, published/updated dates, table of contents, key takeaways, sources, share buttons (§8). [H]
  - المقالات تضيف: صندوق الكاتب، وتاريخ النشر والتحديث، وفهرس المحتويات، وأهم النقاط، والمصادر، وأزرار المشاركة (§8). [H]
- [ ] Detail pages (service/product/tool) add: price or pricing model, proof (reviews, case study), FAQ, related items (§14.2). [H]
  - صفحات التفاصيل (خدمة/منتج/أداة) تضيف: السعر أو نموذج التسعير، والإثبات (مراجعات، دراسة حالة)، والأسئلة الشائعة، والعناصر ذات الصلة (§14.2). [H]
- [ ] Listing/category pages add: unique intro text, filters that don't create indexable duplicates, crawlable pagination.
  - صفحات القوائم والتصنيفات تضيف: مقدمة فريدة، وفلاتر لا تنشئ نسخاً مكررة قابلة للفهرسة، وترقيماً قابلاً للزحف.

**Global footer · التذييل العام**
- [ ] Brand line, contact details (identical to the contact page and schema), links to About, Contact, Privacy, Terms, Cookie preferences (if any), HTML sitemap, official social profiles, language switcher, copyright year. [H]
  - سطر العلامة، وبيانات التواصل (مطابقة لصفحة التواصل والمخطط)، وروابط من نحن والتواصل والخصوصية والشروط وتفضيلات ملفات الارتباط (إن وُجدت) وخريطة HTML والحسابات الرسمية ومبدّل اللغة وسنة الحقوق. [H]

### 35.3 Root and well-known files · ملفات الجذر وwell-known

| Path · المسار | Level · المستوى | Rules · القواعد |
|---|---|---|
| `/robots.txt` | Required<br>إلزامي | 200, UTF-8 text, groups per §1.1, `Sitemap:` line<br>يعيد 200 ونصاً UTF-8 ومجموعات وفق §1.1 وسطر `Sitemap:` |
| `/sitemap.xml` (or index) | Required<br>إلزامي | §9; image/video/news sitemaps only when relevant<br>وفق §9؛ وخرائط الصور والفيديو والأخبار عند الحاجة فقط |
| `/favicon.ico` + SVG/PNG icons | Required<br>إلزامي | Square, at least 48×48 (multiples of 48 recommended), crawlable, `<link rel="icon">` in head<br>مربعة، 48×48 على الأقل (ويُفضّل مضاعفات 48)، قابلة للزحف، ومعلنة في head |
| `/apple-touch-icon.png` | Recommended<br>موصى به | 180×180 PNG, no transparency<br>‏PNG بمقاس 180×180 بلا شفافية |
| `/site.webmanifest` (or `manifest.json`) | Recommended<br>موصى به | `name`, `short_name`, `icons` (192 & 512), `start_url`, `display`, `theme_color`, `background_color`, `lang`, `dir`<br>الحقول الأساسية مع اللغة والاتجاه |
| `/.well-known/security.txt` | Recommended<br>موصى به | RFC 9116: `Contact` and `Expires` required, served over HTTPS<br>‏RFC 9116: الحقلان `Contact` و`Expires` إلزاميان، عبر HTTPS |
| `/llms.txt` (+ `/llms-full.txt`) | Recommended (optional for Google)<br>موصى به (لا يؤثر في Google) | §17 rules, generated from real routes<br>وفق §17 ويُولَّد من المسارات الحقيقية |
| `/feed.xml` (RSS/Atom) | Conditional: blog/news<br>مشروط: مدونة/أخبار | Linked from `<head>` with `rel="alternate"`, one feed per language<br>مرتبط من head، وموجز لكل لغة |
| IndexNow key file `/<key>.txt` | Recommended<br>موصى به | Matches the key used in submissions (§1)<br>يطابق المفتاح المستخدم في الإرسال |
| `/ads.txt` / `/app-ads.txt` | Conditional: programmatic ads<br>مشروط: إعلانات برمجية | IAB format, authorized sellers only<br>صيغة IAB والبائعون المعتمدون فقط |
| `/.well-known/assetlinks.json` | Conditional: Android app<br>مشروط: تطبيق أندرويد | Android App Links; `application/json`<br>روابط تطبيق أندرويد |
| `/.well-known/apple-app-site-association` | Conditional: iOS app<br>مشروط: تطبيق iOS | Universal Links; no file extension; `application/json`<br>الروابط العامة؛ بلا امتداد |
| `/.well-known/change-password` | Optional<br>اختياري | Redirect to the change-password page<br>تحويل لصفحة تغيير كلمة المرور |
| `/humans.txt`, `/opensearch.xml` | Optional<br>اختياري | Team credits; browser search integration<br>شكر الفريق؛ والتكامل مع بحث المتصفح |
| `/.well-known/api-catalog`, `agent-card.json`, `ai-catalog.json` | Conditional: real APIs/agents only<br>مشروط: عند وجود APIs أو وكلاء فعلاً | §17; real 404 otherwise<br>وفق §17؛ وإلا فـ 404 حقيقية |
| Search-engine verification (DNS TXT preferred; or file/meta) | Required<br>إلزامي | Google, Bing (+ Yandex/Naver/Baidu if targeted); keep tokens permanently<br>Google وBing (والمحركات الإقليمية عند الحاجة)؛ وأبقِ رموز التحقق دائماً |

### 35.4 Complete `<head>` checklist · قائمة `<head>` الكاملة

| Tag · الوسم | Level · المستوى | Rule · القاعدة |
|---|---|---|
| `<html lang dir>` | Required | Correct per page (§20, §21) · صحيحة لكل صفحة |
| `<meta charset="utf-8">` | Required | First in head · أول عنصر |
| `<meta name="viewport">` | Required | `width=device-width, initial-scale=1` |
| `<title>` | Required | Unique (§8, §20.2) · فريد |
| `<meta name="description">` | Required | Unique (§8) · فريد |
| `<link rel="canonical">` | Required (indexable pages) | Absolute, self (§2) · مطلق ويشير للذات |
| `<meta name="robots">` | Required when non-default | `noindex` only on purpose; snippet controls (§22.6) · منع الفهرسة عن قصد فقط |
| `<link rel="alternate" hreflang>` | Conditional: multilingual | §10 · وفق §10 |
| Open Graph + Twitter | Required | §8 · وفق §8 |
| JSON-LD `@graph` | Required | §12 · وفق §12 |
| Icons + manifest | Required | `rel="icon"`, `apple-touch-icon`, `rel="manifest"` |
| `theme-color`, `color-scheme` | Recommended | Match light/dark themes · تطابق الوضعين الفاتح والداكن |
| `preconnect` / `preload` | Recommended | Only for critical origins and the LCP asset (§7) · للمصادر الحرجة وأصل LCP فقط |
| RSS/Atom alternate | Conditional | §26.1 · وفق §26.1 |
| Verification meta tags | Optional | Prefer DNS verification · فضّل التحقق عبر DNS |

### 35.5 HTTP & server settings · إعدادات HTTP والخادم

| Situation · الحالة | Correct response · الاستجابة الصحيحة |
|---|---|
| Normal page · صفحة عادية | `200` + `Content-Type: text/html; charset=utf-8` |
| Permanent move, http→https, non-canonical host · نقل دائم وتحويل البروتوكول والنطاق | `301` (or `308`), one hop · قفزة واحدة |
| Temporary redirect (A/B, geo selector) · تحويل مؤقت | `302` / `307` |
| Not found · غير موجود | `404` (custom page) · مع صفحة مخصصة |
| Permanently removed · محذوف نهائياً | `410` |
| Rate limiting bots · تقييد معدل البوتات | `429` (short periods only) · لفترات قصيرة فقط |
| Maintenance / overload · صيانة أو ضغط | `503` + `Retry-After` (hours, not days) · لساعات وليس أياماً |
| Non-HTML files to keep out of index (PDF etc.) · ملفات غير HTML لا تُفهرس | `X-Robots-Tag: noindex` |

- [ ] Security headers on every HTML response: `Strict-Transport-Security`, `Content-Security-Policy` (or at least `frame-ancestors`), `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy`; no `X-Powered-By`/server version. [H]
  - ترويسات الأمان في كل استجابة HTML: HSTS وCSP (أو على الأقل `frame-ancestors`) و`nosniff` و`Referrer-Policy` و`Permissions-Policy`؛ وبلا كشف للإصدار. [H]
- [ ] Caching: hashed static assets `Cache-Control: public, max-age=31536000, immutable`; HTML short-lived or revalidated; never `no-store` on public pages (breaks bfcache). [M]
  - التخزين المؤقت: الملفات الثابتة ذات البصمة لسنة مع `immutable`؛ وHTML لمدة قصيرة أو مع إعادة التحقق؛ ولا `no-store` على الصفحات العامة. [M]
- [ ] Compression (Brotli or gzip) for text; HTTP/2 or HTTP/3; TLS 1.2+ with auto-renewing certificates. [M]
  - ضغط النصوص (Brotli أو gzip)؛ وHTTP/2 أو HTTP/3؛ وTLS 1.2 أو أحدث مع تجديد تلقائي للشهادات. [M]
- [ ] URL normalization rules in one place: one host, HTTPS, lowercase, trailing-slash policy, duplicate slashes, default document (`/index.html` → `/`). [H]
  - قواعد توحيد الروابط في مكان واحد: نطاق واحد، وHTTPS، وأحرف صغيرة، وسياسة الشرطة النهائية، والشرطات المكررة، والمستند الافتراضي. [H]
- [ ] Non-production environments: authentication + `X-Robots-Tag: noindex` + a guard that production can never ship them (§32.1). [C]
  - البيئات غير الإنتاجية: تسجيل دخول + `X-Robots-Tag: noindex` + حماية تمنع وصولها للإنتاج (§32.1). [C]

### 35.6 Accounts & platform settings · الحسابات وإعدادات المنصات

- [ ] **Google Search Console:** Domain property verified by DNS; sitemap index submitted; owners/users reviewed; email alerts on; check Page indexing, Core Web Vitals, HTTPS, Manual actions, Security issues, Crawl stats and AI-related controls monthly. [C]
  - **Google Search Console:** خاصية النطاق موثّقة عبر DNS؛ وفهرس خريطة الموقع مُرسل؛ والمالكون والمستخدمون مراجعون؛ والتنبيهات مفعّلة؛ ومراجعة الفهرسة وCWV وHTTPS والإجراءات اليدوية والمشكلات الأمنية وإحصاءات الزحف وضوابط الذكاء الاصطناعي شهرياً. [C]
- [ ] **Bing Webmaster Tools:** imported or verified, sitemap submitted, IndexNow active. [H]
  - **Bing Webmaster Tools:** مستورد أو موثّق، وخريطة الموقع مرسلة، وIndexNow مفعّل. [H]
- [ ] **Analytics:** consent-aware setup (§27), internal-traffic filter, cross-domain where needed, Search Console link, a custom channel or segment for AI referrers (§22.9), maximum data retention allowed by policy.
  - **التحليلات:** إعداد يحترم الموافقة (§27)، وفلتر الزيارات الداخلية، وتتبع النطاقات المتعددة عند الحاجة، وربط Search Console، وقناة أو شريحة مخصصة لإحالات الذكاء الاصطناعي (§22.9)، وأطول مدة احتفاظ تسمح بها السياسة.
- [ ] **CMS:** production allows indexing (e.g. WordPress "Discourage search engines" unchecked), staging password-protected, clean permalinks, correct language and time zone. [C]
  - **نظام إدارة المحتوى:** الإنتاج يسمح بالفهرسة (مثل إلغاء خيار "منع محركات البحث" في WordPress)، والتجربة محمية بكلمة مرور، وروابط دائمة نظيفة، ولغة ومنطقة زمنية صحيحتان. [C]
- [ ] **CDN / WAF:** verified search and AI-search bots allowed, no challenge pages on content, HTML caching rules that respect cookies and language, image optimization and Brotli on. [H]
  - **CDN / WAF:** السماح للبوتات الموثّقة للبحث والبحث بالذكاء الاصطناعي، ولا صفحات تحدٍّ على المحتوى، وقواعد تخزين HTML تراعي ملفات الارتباط واللغة، وتحسين الصور وBrotli مفعّلان. [H]
- [ ] **DNS & domain:** apex and `www` both resolve and redirect to the canonical host, auto-renewing domain and certificate, CAA record; email authentication (SPF, DKIM, DMARC) to protect the brand (trust, not a ranking factor).
  - **DNS والنطاق:** النطاق الأساسي و`www` يعملان ويحوّلان للنطاق المعتمد، وتجديد تلقائي للنطاق والشهادة، وسجل CAA؛ ومصادقة البريد (SPF وDKIM وDMARC) لحماية العلامة (للثقة وليس عاملاً للترتيب).
- [ ] **Business profiles:** Google Business Profile, Bing Places, Apple Business Connect (local), Merchant Center (e-commerce), official social profiles (§23.1).
  - **الملفات التجارية:** ملف Google التجاري وBing Places وApple Business Connect (للمحلي)، وMerchant Center (للمتاجر)، والحسابات الرسمية (§23.1).
- [ ] **Monitoring:** uptime and TTFB monitoring, certificate-expiry alerts, real-user CWV (RUM) where possible.
  - **المراقبة:** مراقبة التشغيل وTTFB، وتنبيهات انتهاء الشهادة، وبيانات CWV من المستخدمين الحقيقيين حيث أمكن.

### 35.7 Blueprint audit report · تقرير تدقيق مخطط الموقع

When auditing a site, output this table for every row of §35.1, §35.3, §35.4 and every item of §35.2, §35.5, §35.6, then the top 10 actions ordered by level and severity.
عند تدقيق موقع، أخرج هذا الجدول لكل صف في §35.1 و§35.3 و§35.4 ولكل بند في §35.2 و§35.5 و§35.6، ثم أهم 10 إجراءات مرتبة حسب المستوى والخطورة.

| Item · البند | Level · المستوى | Status · الحالة | Evidence (URL / header / file) · الدليل | Action · الإجراء | Severity |
|---|---|---|---|---|---|
| e.g. Privacy policy | Required | Missing · غير موجودة | `/privacy` → 404 | Publish a privacy policy in every language and link it in the footer · انشر سياسة خصوصية بكل لغة واربطها في التذييل | [H] |
| e.g. `/.well-known/security.txt` | Recommended | Exists, expired · موجود ومنتهي | `Expires: 2025-01-01` | Renew `Expires` · جدّد تاريخ الانتهاء | [L] |

Status values · قيم الحالة: OK · Missing · Wrong · Not indexable (but should be) · Indexable (but shouldn't be) · n.a. — موجود وسليم · غير موجود · خاطئ · غير قابل للفهرسة (ويجب أن يكون) · قابل للفهرسة (ولا يجب) · لا ينطبق.

---

## 36. Special cases · حالات خاصة

### 36.1 SaaS & web apps · تطبيقات SaaS والويب
- [ ] Separate the public marketing site (indexable, server-rendered) from the logged-in app (authenticated, `noindex`); keep both on the same registrable domain, preferably in subfolders, unless there is a strong reason for subdomains. [H]
  - افصل موقع التسويق العام (قابل للفهرسة ومن الخادم) عن التطبيق بعد تسجيل الدخول (محمي و`noindex`)؛ وأبقهما على النطاق نفسه ويُفضّل في مجلدات فرعية ما لم يوجد سبب قوي للنطاقات الفرعية. [H]
- [ ] Public, shareable app outputs (reports, profiles, certificates) are indexable only when they are useful to searchers and the owner opted in; otherwise `noindex` and excluded from the sitemap.
  - مخرجات التطبيق العامة القابلة للمشاركة (تقارير، ملفات، شهادات) تُفهرس فقط إن كانت مفيدة للباحثين ووافق صاحبها؛ وإلا `noindex` واستبعاد من خريطة الموقع.
- [ ] Integration, template and use-case pages follow the programmatic gates (§14.3).
  - صفحات التكاملات والقوالب وحالات الاستخدام تخضع لضوابط الصفحات المولّدة (§14.3).

### 36.2 Faceted navigation & URL parameters · التصفية متعددة الأوجه ومعاملات الروابط
- [ ] Decide per filter: indexable landing page (real demand, unique intro, self canonical, in sitemap) or non-indexable (canonical to the base, `noindex`, or not linked). Only a small, deliberate set of filter combinations is indexable. [H]
  - قرّر لكل فلتر: صفحة هبوط قابلة للفهرسة (طلب حقيقي، ومقدمة فريدة، وcanonical ذاتي، وفي خريطة الموقع) أو غير قابلة للفهرسة (canonical للأساس أو `noindex` أو دون ربط). ومجموعة صغيرة مقصودة فقط من التركيبات قابلة للفهرسة. [H]
- [ ] Stable parameter order, no session IDs in URLs, tracking parameters (`utm_*`, `gclid`, `fbclid`) never in internal links and always canonicalized away.
  - ترتيب ثابت للمعاملات، ولا معرّفات جلسات في الروابط، ومعاملات التتبع لا تظهر في الروابط الداخلية وتُزال دائماً عبر canonical.
- [ ] Block infinite crawl spaces (calendars, endless sort/filter combinations) with robots rules or by not linking them — after confirming they hold no unique content.
  - امنع مساحات الزحف اللانهائية (التقويمات، وتركيبات الفرز والتصفية اللانهائية) بقواعد robots أو بعدم ربطها — بعد التأكد أنها بلا محتوى فريد.

### 36.3 Expired, seasonal & out-of-stock content · المحتوى المنتهي والموسمي ونافد المخزون
- [ ] Temporarily out of stock: keep `200`, show availability and alternatives, `availability: OutOfStock` in schema. [H]
  - نفاد مؤقت: أبقِ `200`، واعرض حالة التوفر والبدائل، و`OutOfStock` في المخطط. [H]
- [ ] Permanently discontinued: `301` to the closest replacement or category if one truly exists; otherwise `410` (or keep a useful archive page with `200`).
  - متوقف نهائياً: `301` لأقرب بديل أو تصنيف إن وُجد فعلاً؛ وإلا `410` (أو أبقِ صفحة أرشيف مفيدة بحالة `200`).
- [ ] Recurring events and seasonal pages: one evergreen URL updated every year (e.g. `/black-friday`), not a new URL per year.
  - الفعاليات المتكررة والصفحات الموسمية: رابط دائم واحد يُحدَّث كل عام (مثل `/black-friday`)، وليس رابطاً جديداً كل سنة.
- [ ] Expired jobs and past events: remove from the sitemap, update `validThrough` / event status, and return `404`/`410` or a clear "closed" page.
  - الوظائف المنتهية والفعاليات الماضية: احذفها من خريطة الموقع، وحدّث `validThrough` أو حالة الفعالية، وأعد `404`/`410` أو صفحة "مغلقة" واضحة.

### 36.4 PDFs & documents · ملفات PDF والمستندات
- [ ] Important content lives in HTML; PDFs are secondary downloads. If a PDF must rank: real title in document properties, text (not scanned images), language set, links back to the site. [M]
  - المحتوى المهم في HTML؛ وملفات PDF تنزيلات ثانوية. وإن لزم أن يُفهرس PDF: عنوان حقيقي في خصائص الملف، ونص وليس صوراً ممسوحة، ولغة محددة، وروابط للموقع. [M]
- [ ] Duplicate HTML/PDF versions: `Link: <html-url>; rel="canonical"` header on the PDF, or `X-Robots-Tag: noindex` on it.
  - النسخ المكررة HTML/PDF: ترويسة `Link` بـ canonical نحو صفحة HTML، أو `X-Robots-Tag: noindex` على الملف.

### 36.5 User-generated content · المحتوى الذي ينشئه المستخدمون
- [ ] Links in comments, profiles and forums use `rel="ugc nofollow"`; spam filtering and moderation before content is indexable. [H]
  - الروابط في التعليقات والملفات والمنتديات تحمل `rel="ugc nofollow"`؛ مع فلترة السبام والإشراف قبل أن يصبح المحتوى قابلاً للفهرسة. [H]
- [ ] Thin or empty profiles and threads are `noindex` until they have meaningful content.
  - الملفات والنقاشات الضعيفة أو الفارغة تكون `noindex` حتى يصبح فيها محتوى ذو معنى.

### 36.6 Subdomains, subfolders & multiple domains · النطاقات الفرعية والمجلدات والنطاقات المتعددة
- [ ] Prefer subfolders (`/blog`, `/help`, `/ar`) for content that should share the main site's authority; use subdomains for genuinely separate products or infrastructure.
  - فضّل المجلدات الفرعية (`/blog` و`/help` و`/ar`) للمحتوى الذي يجب أن يشارك قوة الموقع الرئيسي؛ والنطاقات الفرعية للمنتجات أو البنى المنفصلة فعلاً.
- [ ] Several brands or country domains: each has its own sitemap, Search Console property and consistent cross-domain hreflang (§10) where content is equivalent; never duplicate the same content across domains without canonical/hreflang.
  - عدة علامات أو نطاقات دول: لكل منها خريطة موقع وخاصية Search Console وhreflang متسق بين النطاقات (§10) حيث يتطابق المحتوى؛ ولا تكرر المحتوى نفسه بين النطاقات دون canonical/hreflang.

### 36.7 Mobile apps · تطبيقات الجوال
- [ ] App deep links: Android App Links and iOS Universal Links via the well-known files (§35.3), with the same URL on web and app.
  - الروابط العميقة: روابط تطبيقات أندرويد والروابط العامة في iOS عبر ملفات well-known (§35.3)، بنفس الرابط على الويب والتطبيق.
- [ ] Promote the app without interstitials that hide content (use small banners / Smart App Banner); app store pages linked from the site and listed in `sameAs`.
  - روّج للتطبيق دون نوافذ تحجب المحتوى (شرائط صغيرة أو Smart App Banner)؛ واربط صفحات المتاجر من الموقع وأدرجها في `sameAs`.

---

## 37. Definition of done · تعريف الإنجاز


- All applicable [C] and [H] items pass **in every locale** and are covered by automated tests (run head/hreflang/JSON-LD tests per language, incl. RTL `dir` and `inLanguage`).
  - كل بنود [C] و[H] المنطبقة ناجحة **في كل لغة** ومغطاة باختبارات آلية (شغّل اختبارات head/hreflang/JSON-LD لكل لغة، بما فيها `dir` لـ RTL و`inLanguage`).
- AEO: question bank per language exists, top pages follow the answer-block pattern, facts page and glossary are live, AI-referral tracking is configured.
  - AEO: يوجد بنك أسئلة لكل لغة، والصفحات الأهم تتبع نمط كتلة الإجابة، وصفحة الحقائق والمسرد منشورتان، وتتبّع الإحالات من الذكاء الاصطناعي مُعدّ.
- Central SEO head component + JSON-LD builder in place; sitemap, robots.txt (and llms.txt if chosen) generated from real data.
  - مكوّن SEO مركزي لـ head + مُنشئ JSON-LD جاهزان؛ وخريطة الموقع وrobots.txt (وllms.txt إن اختير) تُولَّد من بيانات حقيقية.
- Owner-input list delivered (AI-training policy, NAP, social profiles, author credentials, etc.).
  - تسليم قائمة مدخلات المالك (سياسة تدريب الذكاء الاصطناعي، الاسم والعنوان والهاتف، حسابات التواصل، مؤهلات الكتّاب، إلخ).
- Final report: fixed / skipped (with reason) / needs owner / production-only verification.
  - التقرير النهائي: ما أُصلح / ما تم تجاوزه (مع السبب) / ما يحتاج المالك / ما يُتحقق منه في الإنتاج فقط.

- The §30 verification kit runs on production with **zero [C]**; SEO and AEO scores (§31) are recorded with the date.
  - أدوات التحقق في §30 تعمل على الإنتاج **دون أي [C]**؛ ودرجتا SEO وAEO (§31) مسجلتان بالتاريخ.
- CI gates (§32.1) are active and the review cadence (§32.2) has named owners.
  - بوابات CI (§32.1) مفعّلة، ولجدول المراجعة (§32.2) مسؤولون محددون.
- Share-of-voice and off-site baselines (§23, §24.3) are recorded; consent behavior is verified (§27); the migration checklist (§25) is complete when a migration happened.
  - خطوط أساس نسبة الظهور والحضور الخارجي (§23، §24.3) مسجلة؛ وسلوك الموافقة متحقق منه (§27)؛ وقائمة النقل (§25) مكتملة عند حدوث نقل.
- Audit mode: the §35.7 blueprint report lists every required page, file and setting with its status, and the §36 special cases that apply are handled.
  - وضع التدقيق: تقرير مخطط الموقع §35.7 يذكر كل صفحة وملف وإعداد إلزامي مع حالته، والحالات الخاصة المنطبقة في §36 معالجة.
