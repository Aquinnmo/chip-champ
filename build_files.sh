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

# List staticfiles directory to verify collection
echo "Static files collected. Contents of staticfiles directory:"
ls -la staticfiles/

# Ensure staticfiles directory has proper permissions
chmod -R 755 staticfiles/

echo "Build script completed!"
