#!/usr/bin/env python3
"""
Quick test to verify static files are working correctly
"""
import requests
import sys
import time

def test_static_files():
    base_url = "http://127.0.0.1:8000"
    
    print("Testing static files serving...")
    
    # Wait a moment for server to be ready
    time.sleep(2)
    
    # Test static file URLs
    static_files = [
        "/static/css/style.css",
        "/static/images/cc_logo.png", 
        "/static/js/main.js"
    ]
    
    print(f"\nTesting static files at {base_url}:")
    all_good = True
    
    for static_file in static_files:
        url = f"{base_url}{static_file}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✓ {static_file} - Status: {response.status_code}, Size: {len(response.content)} bytes")
            else:
                print(f"✗ {static_file} - Status: {response.status_code}")
                all_good = False
        except requests.exceptions.RequestException as e:
            print(f"✗ {static_file} - Error: {e}")
            all_good = False
    
    # Test homepage to see if static files are linked
    try:
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            content = response.text
            if '/static/css/style.css' in content:
                print("✓ CSS link found in homepage HTML")
            else:
                print("✗ CSS link not found in homepage HTML")
                all_good = False
                
            if '/static/images/cc_logo.png' in content:
                print("✓ Logo image found in homepage HTML")  
            else:
                print("✗ Logo image not found in homepage HTML")
                all_good = False
        else:
            print(f"✗ Homepage failed to load: {response.status_code}")
            all_good = False
    except Exception as e:
        print(f"✗ Error testing homepage: {e}")
        all_good = False
    
    return all_good

if __name__ == '__main__':
    try:
        import requests
    except ImportError:
        print("Installing requests...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
    
    success = test_static_files()
    if success:
        print("\n🎉 All static files are working correctly!")
        print("Your static files setup is ready for deployment.")
    else:
        print("\n❌ Some static files are not working correctly.")
        print("Check the errors above.")
