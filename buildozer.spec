[app]
# عنوان التطبيق
title = Simple Calculator

# اسم الحزمة (Package name)
package.name = calculator

# النطاق (Package domain)
package.domain = org.calc

# الملفات المراد تضمينها في التطبيق
source.include_exts = py,png,jpg,kv,atlas

# ملف البداية الأساسي لتطبيقك
source.main_file = calculator.py

# الإصدار
version = 0.1

# المتطلبات (يعتمد التطبيق هنا على tkinter أو kivy، ولكي يعمل بناء أندرويد بسهولة وبأقل تعقيد لمكتبات سطح المكتب التي لا تدعم أندرويد مباشرة، يُفضل استخدام إطار عمل Kivy للواجهات في أندرويد، أو استخدام سكربت مبسط لجيثب).
requirements = python3,kivy

# الاتجاه والأذونات
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
