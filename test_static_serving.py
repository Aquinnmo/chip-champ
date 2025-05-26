#!/usr/bin/env python3
"""
Quick test to verify static files are served correctly
"""
import requests
import sys

def test_static_files_serving():
    base_url = "http://127.0.0.1:8000"
    
    print("Testing static files serving...")
    
    # Test if server is running
    try:
        response = requests.get(base_url, timeout=5)
        print(f"✓ Server is running - Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"✗ Server not reachable: {e}")
        return False
    
    # Test static file URLs
    static_files = [
        "/static/css/style.css",
        "/static/images/cc_logo.png",
        "/static/js/main.js"
    ]
    
    print("\nTesting static file URLs:")
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
    
    # Test if CSS is actually in the HTML
    try:
        response = requests.get(base_url)
        html_content = response.text
        if '/static/css/style.css' in html_content:
            print("✓ CSS link found in homepage HTML")
        else:
            print("✗ CSS link not found in homepage HTML")
            all_good = False
            
        if '/static/images/cc_logo.png' in html_content:
            print("✓ Logo image link found in homepage HTML")
        else:
            print("✗ Logo image link not found in homepage HTML")
            all_good = False
            
    except Exception as e:
        print(f"✗ Error checking HTML content: {e}")
        all_good = False
    
    return all_good

if __name__ == '__main__':
    success = test_static_files_serving()
    if success:
        print("\n🎉 All static files are being served correctly!")
        print("Your static files setup is working. You can deploy to Vercel.")
    else:
        print("\n❌ Some static files are not being served correctly.")
        print("Check the Django development server and ensure it's running.")
