#!/usr/bin/env python3
"""
Test script to verify static files configuration
"""
import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
os.environ.setdefault('VERCEL_ENV', 'production')
os.environ.setdefault('DEBUG', 'False')

# Setup Django
django.setup()

from django.conf import settings
from django.core.management import call_command
from django.contrib.staticfiles import finders

def test_static_files():
    print("Testing static files configuration...")
    print(f"STATIC_URL: {settings.STATIC_URL}")
    print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
    print(f"STATICFILES_STORAGE: {settings.STATICFILES_STORAGE}")
    
    # Test finding specific static files
    test_files = [
        'css/style.css',
        'images/cc_logo.png',
        'js/main.js'
    ]
    
    print("\nTesting static file finding:")
    for file_path in test_files:
        found = finders.find(file_path)
        if found:
            print(f"✓ Found: {file_path} at {found}")
        else:
            print(f"✗ Not found: {file_path}")
    
    # Collect static files
    print("\nCollecting static files...")
    try:
        call_command('collectstatic', '--noinput', '--clear', '--verbosity=2')
        print("✓ Static files collected successfully")
        
        # Check if files exist in STATIC_ROOT
        static_root = Path(settings.STATIC_ROOT)
        if static_root.exists():
            print(f"\nContents of {static_root}:")
            for item in static_root.rglob('*'):
                if item.is_file():
                    print(f"  {item.relative_to(static_root)}")
        
    except Exception as e:
        print(f"✗ Static files collection failed: {e}")

if __name__ == '__main__':
    test_static_files()
