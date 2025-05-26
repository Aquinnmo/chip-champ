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

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear --verbosity=2

# Verify staticfiles_build directory was created and populated
echo "Verifying static files collection..."
if [ -d "staticfiles_build" ]; then
    echo "✓ staticfiles_build directory exists"
    file_count=$(find staticfiles_build -type f | wc -l)
    echo "✓ Found $file_count files in staticfiles_build"
    
    # Check for critical files
    if [ -f "staticfiles_build/css/style.css" ]; then
        echo "✓ CSS file found"
    else
        echo "⚠ CSS file not found in staticfiles_build"
    fi
    
    if [ -f "staticfiles_build/images/cc_logo.png" ]; then
        echo "✓ Logo file found"
    else
        echo "⚠ Logo file not found in staticfiles_build"
    fi
else
    echo "✗ staticfiles_build directory not found!"
    echo "Attempting to create and populate staticfiles_build..."
    
    # Create directory manually
    mkdir -p staticfiles_build
    
    # Check if staticfiles exists (old default location)
    if [ -d "staticfiles" ]; then
        echo "Found staticfiles directory, copying to staticfiles_build..."
        cp -r staticfiles/* staticfiles_build/
    else
        echo "Creating minimal staticfiles_build structure..."
        mkdir -p staticfiles_build/css
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
