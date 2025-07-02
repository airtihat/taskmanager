import polib

# تحميل ملف الترجمة العربي
po = polib.pofile("django_ar.po")

# إنشاء ملف ترجمة معكوس (عربي → إنجليزي)
reversed_po = polib.POFile()
reversed_po.metadata = po.metadata

for entry in po:
    if entry.msgstr.strip():
        reversed_entry = entry.clone()
        reversed_entry.msgid, reversed_entry.msgstr = entry.msgstr, entry.msgid
        reversed_po.append(reversed_entry)

# حفظ الملف الجديد
reversed_po.save("django_ar_to_en.po")
print("✅ تم توليد الملف: django_ar_to_en.po")
