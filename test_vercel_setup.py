#!/usr/bin/env python3
"""
Script to test Vercel deployment setup locally
"""
import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and print the result"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Success")
            if result.stdout:
                print(f"Output: {result.stdout.strip()}")
        else:
            print(f"❌ {description} - Failed")
            if result.stderr:
                print(f"Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ {description} - Exception: {e}")
        return False
    return True

def main():
    print("🚀 Testing Vercel deployment setup...")
    
    # Check if we're in the right directory
    if not Path("manage.py").exists():
        print("❌ Not in Django project directory. Please run from project root.")
        sys.exit(1)
    
    # Check required files
    required_files = ["vercel.json", "build_files.sh", "vercel_app.py", "requirements.txt"]
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            return False
    
    # Test environment setup
    print("\n📋 Testing deployment setup...")
    
    # Check Python dependencies
    if not run_command("python -m pip list | findstr Django", "Checking Django installation"):
        print("⚠️  Django not installed. Run: pip install -r requirements.txt")
    
    # Test static file collection
    if not run_command("python manage.py collectstatic --noinput --dry-run", "Testing static file collection"):
        return False
    
    # Test Django check
    if not run_command("python manage.py check", "Django system check"):
        return False
    
    print("\n🎉 Vercel deployment setup looks good!")
    print("\n📝 Next steps:")
    print("1. Push your code to GitHub/GitLab/Bitbucket")
    print("2. Connect your repository to Vercel")
    print("3. Set environment variables in Vercel dashboard")
    print("4. Deploy!")
    
    return True

if __name__ == "__main__":
    main()
