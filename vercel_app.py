import os
import sys
import django
from django.core.wsgi import get_wsgi_application

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set environment variables for production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
os.environ.setdefault('VERCEL_ENV', 'production')

# Setup Django
django.setup()

# Collect static files during deployment
try:
    from django.core.management import call_command
    print("Starting static files collection...")
    call_command('collectstatic', '--noinput', '--clear', '--verbosity=2')
    print("Static files collected successfully")
    
    # Verify critical files exist
    from django.conf import settings
    import os
    static_root = str(settings.STATIC_ROOT)
    css_file = os.path.join(static_root, 'css', 'style.css')
    logo_file = os.path.join(static_root, 'images', 'cc_logo.png')
    
    if os.path.exists(css_file):
        print(f"✓ CSS file exists: {css_file}")
    else:
        print(f"✗ CSS file missing: {css_file}")
        
    if os.path.exists(logo_file):
        print(f"✓ Logo file exists: {logo_file}")
    else:
        print(f"✗ Logo file missing: {logo_file}")
        
except Exception as e:
    print(f"Static files collection failed: {e}")
    import traceback
    traceback.print_exc()

application = get_wsgi_application()

# Vercel requires the application to be named 'app'
app = application
