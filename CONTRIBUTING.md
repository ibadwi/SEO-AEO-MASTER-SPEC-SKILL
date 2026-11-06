# Contributing · المساهمة

Thank you for helping keep this spec accurate. · شكراً لمساهمتك في إبقاء هذه المواصفة دقيقة.

## Rules · القواعد

1. **Cite a primary source** for every factual change (Google Search Central, Bing, schema.org, W3C/IETF, the crawler owner's docs, the framework's official docs). Blog posts and tools are fine as supporting evidence, not as the only source.
   **اذكر مصدراً رسمياً** لكل تعديل في الحقائق. المدونات والأدوات تصلح كدليل داعم فقط.
2. **Edit both languages.** Every requirement is one English line plus its Arabic sub-bullet; keep their meaning identical and keep **one checkbox per requirement**.
   **عدّل اللغتين معاً.** كل متطلب سطر إنجليزي وتحته سطره العربي؛ بالمعنى نفسه ومربع اختيار واحد.
3. **Label heuristics.** Third-party observations and numeric rules of thumb are marked *heuristic* / *إرشادي*; never present them as engine rules.
   **علّم الإرشادات.** ملاحظات الأطراف الثالثة والأرقام التقريبية تُعلَّم بأنها إرشادية.
4. **No promises.** Never claim a change guarantees rankings, traffic or AI citations.
   **لا وعود** بترتيب أو زيارات أو اقتباسات.
5. **Keep section numbers stable.** Add new subsections at the end of a section; don't renumber existing ones (other projects link to them). Update every `§` reference you touch.
   **حافظ على أرقام الأقسام.** أضف الأقسام الفرعية الجديدة في نهاية القسم، وحدّث الإحالات `§`.
6. **Update maintenance info** in §34: "Last verified", and a line in the changelog (§34.4 and `CHANGELOG.md`).
   **حدّث معلومات الصيانة** في §34 وسجل التغييرات.
7. **Script changes:** `scripts/seo_audit.py` is also embedded in §30.3 — keep both copies identical, standard library only, and test it on a page with known errors.
   **تعديلات السكربت:** السكربت موجود أيضاً داخل §30.3 — أبقِ النسختين متطابقتين، ودون مكتبات خارجية، واختبره على صفحة فيها أخطاء معروفة.

## Retiring a rule · إلغاء قاعدة

Don't delete silently: mark it `retired (YYYY-MM, reason, source)` for one release, then remove it.
لا تحذف بصمت: علّمها `متقاعدة (التاريخ، السبب، المصدر)` لإصدار واحد ثم احذفها.

## Pull request checklist · قائمة طلب الدمج

- [ ] Primary source linked in the PR description · مصدر رسمي مرفق
- [ ] English and Arabic both updated · اللغتان محدّثتان
- [ ] `§` references still resolve · الإحالات سليمة
- [ ] "Last verified" and changelog updated · "آخر تحقق" وسجل التغييرات محدّثان
- [ ] Script copies identical and tested (if touched) · نسختا السكربت متطابقتان ومختبرتان
