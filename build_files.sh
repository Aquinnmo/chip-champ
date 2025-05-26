#!/bin/bash

# Build script for Vercel
echo "Build script started..."

# Install Python dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

# Set Django settings for production
export DJANGO_SETTINGS_MODULE=myproject.settings
export DEBUG=False
export VERCEL_ENV=production

# Clean up any existing static files to ensure fresh build
echo "Cleaning up existing static files..."
rm -rf staticfiles_build
mkdir -p staticfiles_build

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear --verbosity=2

# Verify staticfiles_build directory was created and populated
echo "Verifying static files collection..."
if [ -d "staticfiles_build" ]; then
    echo "✓ staticfiles_build directory exists"
    file_count=$(find staticfiles_build -type f | wc -l)
    echo "✓ Found $file_count files in staticfiles_build"
    
    # List the structure for debugging
    echo "Static files structure:"
    find staticfiles_build -type f | head -20
    
    # Check for critical files
    if [ -f "staticfiles_build/css/style.css" ]; then
        echo "✓ CSS file found"
        css_size=$(wc -c < "staticfiles_build/css/style.css")
        echo "  CSS file size: $css_size bytes"
    else
        echo "⚠ CSS file not found in staticfiles_build"
    fi
    
    if [ -f "staticfiles_build/images/cc_logo.png" ]; then
        echo "✓ Logo file found"
        logo_size=$(wc -c < "staticfiles_build/images/cc_logo.png")
        echo "  Logo file size: $logo_size bytes"
    else
        echo "⚠ Logo file not found in staticfiles_build"
    fi
    
    if [ -f "staticfiles_build/js/main.js" ]; then
        echo "✓ JavaScript file found"
    else
        echo "⚠ JavaScript file not found in staticfiles_build"
    fi
else
    echo "✗ staticfiles_build directory not found!"
    echo "Build failed - static files collection unsuccessful"
    exit 1
fi

echo "✓ Static files build completed successfully"
        mkdir -p staticfiles_build/js
        mkdir -p staticfiles_build/images
        
        # Copy from static directory if it exists
        if [ -d "static" ]; then
            cp -r static/* staticfiles_build/
        fi
    fi
fi

# Set proper permissions for staticfiles_build directory
chmod -R 755 staticfiles_build

# List staticfiles_build directory to verify collection
echo "Static files collected. Contents of staticfiles_build directory:"
ls -la staticfiles_build/

echo "Build completed successfully!"

echo "Build script completed!"
