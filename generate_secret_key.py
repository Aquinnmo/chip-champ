#!/usr/bin/env python3
"""
Generate a production-ready Django secret key for Vercel deployment.
Run this script and copy the output to your Vercel environment variables.
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from django.core.management.utils import get_random_secret_key
    
    print("🔑 Generated Django Secret Key for Production:")
    print("=" * 60)
    print(get_random_secret_key())
    print("=" * 60)
    print("\n📝 Instructions:")
    print("1. Copy the secret key above")
    print("2. Go to your Vercel dashboard")
    print("3. Navigate to your project settings")
    print("4. Add environment variable: SECRET_KEY=[paste-key-here]")
    print("5. Set DEBUG=False")
    print("6. Deploy your project")
    
except ImportError:
    print("❌ Django not found. Please install Django first:")
    print("pip install Django")
except Exception as e:
    print(f"❌ Error generating secret key: {e}")
