#!/bin/bash

# Vercel deployment verification script
echo "=== Vercel Deployment Verification ==="
echo "Checking static files setup for Vercel deployment..."

# Check if required files exist
echo ""
echo "1. Checking required files:"
files=("vercel.json" "build_files.sh" "requirements.txt" "vercel_app.py")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✓ $file exists"
    else
        echo "✗ $file missing"
    fi
done

# Check static files structure
echo ""
echo "2. Checking static files structure:"
if [ -d "static" ]; then
    echo "✓ static/ directory exists"
    if [ -f "static/css/style.css" ]; then
        echo "✓ static/css/style.css exists"
    else
        echo "✗ static/css/style.css missing"
    fi
    if [ -f "static/images/cc_logo.png" ]; then
        echo "✓ static/images/cc_logo.png exists"
    else
        echo "✗ static/images/cc_logo.png missing"
    fi
    if [ -f "static/js/main.js" ]; then
        echo "✓ static/js/main.js exists"
    else
        echo "✗ static/js/main.js missing"
    fi
else
    echo "✗ static/ directory missing"
fi

echo ""
echo "3. Testing static files collection:"
python3 manage.py collectstatic --noinput --dry-run | head -20

echo ""
echo "=== Ready for Vercel Deployment ==="
echo "Run: vercel --prod"
echo ""
echo "If you see any ✗ marks above, fix those issues before deploying."
