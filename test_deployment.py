#!/usr/bin/env python3
"""
Test script to check if your deployed site is working correctly
"""
import requests
import re
from urllib.parse import urljoin

def test_deployed_site(base_url):
    """Test if the deployed site is serving static files correctly"""
    
    print(f"Testing deployed site: {base_url}")
    print("=" * 50)
    
    try:
        # Test if the main page loads
        print("1. Testing main page...")
        response = requests.get(base_url, timeout=10)
        
        if response.status_code == 200:
            print("   ✓ Main page loads successfully")
            
            # Check if CSS is linked in the HTML
            html_content = response.text
            css_links = re.findall(r'<link[^>]*href="([^"]*\.css)"[^>]*>', html_content)
            
            if css_links:
                print(f"   ✓ Found {len(css_links)} CSS link(s) in HTML")
                for css_link in css_links:
                    if css_link.startswith('/static/'):
                        print(f"     - {css_link}")
            else:
                print("   ✗ No CSS links found in HTML")
            
            # Check if images are linked
            img_links = re.findall(r'<img[^>]*src="([^"]*)"[^>]*>', html_content)
            static_imgs = [img for img in img_links if img.startswith('/static/')]
            
            if static_imgs:
                print(f"   ✓ Found {len(static_imgs)} static image(s) in HTML")
                for img_link in static_imgs:
                    print(f"     - {img_link}")
            else:
                print("   ✗ No static images found in HTML")
                
        else:
            print(f"   ✗ Main page failed to load: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"   ✗ Error loading main page: {e}")
        return False
    
    # Test static file URLs directly
    print("\n2. Testing static file URLs...")
    
    static_files_to_test = [
        '/static/css/style.css',
        '/static/images/cc_logo.png',
        '/static/js/main.js'
    ]
    
    all_static_working = True
    
    for static_file in static_files_to_test:
        try:
            static_url = urljoin(base_url, static_file)
            response = requests.get(static_url, timeout=10)
            
            if response.status_code == 200:
                content_type = response.headers.get('Content-Type', 'unknown')
                content_length = len(response.content)
                print(f"   ✓ {static_file} - Status: {response.status_code}, Type: {content_type}, Size: {content_length} bytes")
            else:
                print(f"   ✗ {static_file} - Status: {response.status_code}")
                all_static_working = False
                
        except Exception as e:
            print(f"   ✗ {static_file} - Error: {e}")
            all_static_working = False
    
    # Test if styles are actually applied
    print("\n3. Testing CSS content...")
    try:
        css_url = urljoin(base_url, '/static/css/style.css')
        response = requests.get(css_url, timeout=10)
        
        if response.status_code == 200:
            css_content = response.text
            
            # Check for key CSS rules
            if '--primary-color' in css_content and 'body {' in css_content:
                print("   ✓ CSS file contains expected styles")
            else:
                print("   ⚠ CSS file seems incomplete or incorrect")
                
            print(f"   - CSS file size: {len(css_content)} characters")
            
        else:
            print(f"   ✗ CSS file not accessible: {response.status_code}")
            all_static_working = False
            
    except Exception as e:
        print(f"   ✗ Error testing CSS: {e}")
        all_static_working = False
    
    print("\n" + "=" * 50)
    if all_static_working:
        print("🎉 SUCCESS: All static files are working correctly!")
        print("Your deployment should be displaying styles and images properly.")
    else:
        print("❌ ISSUES FOUND: Some static files are not working correctly.")
        print("Check the errors above and review your Vercel configuration.")
    
    return all_static_working

if __name__ == '__main__':
    # You can replace this with your actual Vercel deployment URL
    print("Static Files Deployment Test")
    print("Please enter your Vercel deployment URL (e.g., https://your-app.vercel.app):")
    
    # For testing, you can also hardcode your URL here:
    # deployment_url = "https://your-app.vercel.app"
    
    deployment_url = input("Deployment URL: ").strip()
    
    if not deployment_url:
        print("No URL provided. Exiting.")
        exit(1)
    
    if not deployment_url.startswith('http'):
        deployment_url = 'https://' + deployment_url
    
    test_deployed_site(deployment_url)
