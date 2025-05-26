#!/usr/bin/env python3
"""
Test script to verify static files are working correctly for deployment
"""
import os
import sys
import django
from pathlib import Path
import urllib.request

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set environment variables for production-like testing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
os.environ.setdefault('VERCEL_ENV', 'production')
os.environ.setdefault('DEBUG', 'False')

# Setup Django
django.setup()

from django.conf import settings
from django.core.management import call_command
from django.contrib.staticfiles import finders
from django.test import Client
from django.urls import reverse

def test_static_files_deployment():
    print("Testing static files for deployment...")
    print(f"STATIC_URL: {settings.STATIC_URL}")
    print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"STATICFILES_STORAGE: {settings.STATICFILES_STORAGE}")
    
    # Collect static files
    print("\nCollecting static files...")
    try:
        call_command('collectstatic', '--noinput', '--clear', '--verbosity=1')
        print("✓ Static files collected successfully")
    except Exception as e:
        print(f"✗ Static files collection failed: {e}")
        return False
    
    # Check if static files exist in STATIC_ROOT
    static_root = Path(settings.STATIC_ROOT)
    if not static_root.exists():
        print(f"✗ Static root directory doesn't exist: {static_root}")
        return False
    
    # Test specific files
    test_files = [
        'css/style.css',
        'images/cc_logo.png',
        'js/main.js'
    ]
    
    print("\nChecking static files in STATIC_ROOT:")
    all_files_exist = True
    for file_path in test_files:
        full_path = static_root / file_path
        if full_path.exists():
            print(f"✓ Found: {file_path} ({full_path.stat().st_size} bytes)")
        else:
            print(f"✗ Missing: {file_path}")
            all_files_exist = False
    
    # Test Django's static file serving
    print("\nTesting Django static file serving...")
    client = Client()
    
    try:
        # Test home page loads
        response = client.get('/')
        if response.status_code == 200:
            print("✓ Home page loads successfully")
            
            # Check if static file URLs are in the HTML
            content = response.content.decode()
            if '/static/css/style.css' in content:
                print("✓ CSS link found in HTML")
            else:
                print("✗ CSS link not found in HTML")
                
            if '/static/images/cc_logo.png' in content:
                print("✓ Logo image link found in HTML")
            else:
                print("✗ Logo image link not found in HTML")
        else:
            print(f"✗ Home page failed to load: {response.status_code}")
            all_files_exist = False
            
    except Exception as e:
        print(f"✗ Error testing Django: {e}")
        all_files_exist = False
    
    # Test static file URLs directly
    print("\nTesting static file URLs:")
    for file_path in test_files:
        url = f"{settings.STATIC_URL}{file_path}"
        try:
            response = client.get(url)
            if response.status_code == 200:
                print(f"✓ {url} - Status: {response.status_code}")
            else:
                print(f"✗ {url} - Status: {response.status_code}")
                all_files_exist = False
        except Exception as e:
            print(f"✗ {url} - Error: {e}")
            all_files_exist = False
    
    return all_files_exist

if __name__ == '__main__':
    success = test_static_files_deployment()
    if success:
        print("\n🎉 All static files tests passed! Ready for deployment.")
    else:
        print("\n❌ Some static files tests failed. Check the issues above.")
    
    print("\nNext steps:")
    print("1. If tests passed, deploy with: vercel --prod")
    print("2. After deployment, check browser developer tools for 404 errors")
    print("3. Verify CSS is applied and images load on your live site")
