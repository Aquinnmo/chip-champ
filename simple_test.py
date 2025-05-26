import os
import django
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.conf import settings

print(f"STATIC_URL: {settings.STATIC_URL}")
print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
print(f"STATICFILES_STORAGE: {settings.STATICFILES_STORAGE}")

# Check if files exist
static_root = Path(settings.STATIC_ROOT)
css_file = static_root / 'css' / 'style.css'
logo_file = static_root / 'images' / 'cc_logo.png'

print(f"CSS exists: {css_file.exists()}")
print(f"Logo exists: {logo_file.exists()}")

if css_file.exists():
    print(f"CSS size: {css_file.stat().st_size} bytes")
if logo_file.exists():
    print(f"Logo size: {logo_file.stat().st_size} bytes")
