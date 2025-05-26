import os
import sys
import django
from django.core.wsgi import get_wsgi_application
from django.conf import settings

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Setup Django
django.setup()

# Collect static files during deployment (only in production)
if not settings.DEBUG:
    try:
        from django.core.management import call_command
        call_command('collectstatic', '--noinput', '--clear')
        print("Static files collected successfully")
    except Exception as e:
        print(f"Static files collection failed: {e}")

application = get_wsgi_application()

# Vercel requires the application to be named 'app'
app = application
