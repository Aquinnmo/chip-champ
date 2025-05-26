#!/bin/bash

# Build script for Vercel
echo "Build script started..."

# Install Python dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "Build script completed!"
