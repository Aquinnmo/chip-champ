#!/usr/bin/env python3
"""
Quick verification script for static files setup
"""
import os
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
os.environ.setdefault('VERCEL_ENV', 'production')
os.environ.setdefault('DEBUG', 'False')

django.setup()

from django.conf import settings
from django.core.management import call_command

def verify_static_setup():
    print("Django Static Files Verification")
    print("=" * 40)
    
    print(f"STATIC_URL: {settings.STATIC_URL}")
    print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"STATICFILES_STORAGE: {settings.STATICFILES_STORAGE}")
    print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
    
    # Collect static files
    print("\nCollecting static files...")
    try:
        call_command('collectstatic', '--noinput', '--clear')
        print("✓ Static files collected successfully")
    except Exception as e:
        print(f"✗ Static files collection failed: {e}")
        return False
    
    # Check if files exist
    static_root = Path(settings.STATIC_ROOT)
    if not static_root.exists():
        print(f"✗ Static root doesn't exist: {static_root}")
        return False
    
    # Check specific files
    test_files = {
        'css/style.css': 'CSS file',
        'images/cc_logo.png': 'Logo image',
        'js/main.js': 'JavaScript file'
    }
    
    print(f"\nChecking files in {static_root}:")
    all_good = True
    
    for file_path, description in test_files.items():
        full_path = static_root / file_path
        if full_path.exists():
            size = full_path.stat().st_size
            print(f"✓ {description}: {file_path} ({size} bytes)")
        else:
            print(f"✗ {description}: {file_path} - NOT FOUND")
            all_good = False
    
    # Count total files
    total_files = sum(1 for _ in static_root.rglob('*') if _.is_file())
    print(f"\nTotal static files collected: {total_files}")
    
    return all_good

if __name__ == '__main__':
    success = verify_static_setup()
    
    if success:
        print("\n🎉 Static files setup verified successfully!")
        print("You can now deploy to Vercel with confidence.")
    else:
        print("\n❌ Static files setup has issues.")
        print("Please fix the issues above before deploying.")
    
    print("\nNext steps:")
    print("1. Commit and push your changes to Git")
    print("2. Deploy to Vercel (it will automatically redeploy)")
    print("3. Test your deployment URL with the test_deployment.py script")
