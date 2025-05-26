# Vercel Environment Variables Setup

After fixing the build issues, you'll need to set these environment variables in your Vercel dashboard:

## Required Environment Variables

1. **SECRET_KEY**
   - Value: KEY VALUE

2. **DEBUG**
   - Value: `False`

3. **ALLOWED_HOSTS**
   - Value: `.vercel.app,127.0.0.1,localhost,chip-champ.adam-montgomery.ca`

4. **DJANGO_SETTINGS_MODULE**
   - Value: `myproject.settings`

## How to set them:

1. Go to your Vercel dashboard
2. Select your project
3. Go to Settings → Environment Variables
4. Add each variable with its corresponding value

## Fixed Issues:

✅ **"No Output Directory named 'staticfiles_build' found"** - Fixed by:
- Simplified static files configuration to use `staticfiles` directory
- Updated Django settings to use consistent static files path
- Removed complex conditional static files setup
- Updated `vercel_app.py` to handle static files collection properly

## Note:
- Never commit your `.env` file to version control
- Make sure to add `.env` to your `.gitignore` file
- Static files are now collected to `staticfiles/` directory consistently
