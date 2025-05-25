# 🚀 Vercel Deployment Guide

Your Django project is now ready for deployment on Vercel! Follow these steps to deploy your application.

## 📋 Pre-Deployment Checklist

✅ **Files Configured:**
- `vercel.json` - Vercel configuration with Python 3.11
- `vercel_app.py` - WSGI entry point
- `build_files.sh` - Build script for static files
- `requirements.txt` - Python dependencies
- `.vercelignore` - Files to exclude from deployment
- `.env.production` - Production environment variables template

✅ **Django Settings:**
- Production security settings enabled
- WhiteNoise for static file serving
- CSRF trusted origins configured for your domain
- Database URL support for external databases

## 🔧 Step 1: Environment Variables

In your Vercel dashboard, set these environment variables:

### Required Variables:
```
SECRET_KEY=your-production-secret-key-here
DEBUG=False
ALLOWED_HOSTS=.vercel.app,chip-champ.adam-montgomery.ca
```

### Optional Variables:
```
DATABASE_URL=your-database-url-here
CSRF_TRUSTED_ORIGINS=https://your-app.vercel.app,https://chip-champ.adam-montgomery.ca
```

> **🔑 Generate a Secret Key:** 
> Use Django's built-in command: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

## 🌐 Step 2: Deploy to Vercel

### Option A: Vercel CLI (Recommended)
1. Install Vercel CLI: `npm install -g vercel`
2. Login: `vercel login`
3. Deploy: `vercel --prod`

### Option B: GitHub Integration
1. Push your code to GitHub
2. Connect your GitHub repo to Vercel
3. Automatic deployment will start

## 🔍 Step 3: Post-Deployment

After successful deployment:

1. **Test your application** at your Vercel URL
2. **Check admin panel** at `/admin/`
3. **Verify static files** are loading correctly
4. **Test your custom domain** (chip-champ.adam-montgomery.ca)

## 🐛 Troubleshooting

### Common Issues:

**Static files not loading:**
- Ensure `whitenoise` is in MIDDLEWARE
- Check that `collectstatic` runs during build
- Verify STATIC_URL and STATIC_ROOT settings

**CSRF errors:**
- Add your domain to CSRF_TRUSTED_ORIGINS
- Ensure ALLOWED_HOSTS includes your domain

**Database issues:**
- For production, consider using PostgreSQL
- Set DATABASE_URL environment variable
- SQLite works but has limitations on Vercel

### Vercel Logs:
```bash
vercel logs [deployment-url]
```

## 📝 Domain Configuration

Your custom domain `chip-champ.adam-montgomery.ca` is already configured in:
- ALLOWED_HOSTS
- CSRF_TRUSTED_ORIGINS

To use this domain:
1. Add it in Vercel dashboard under "Domains"
2. Update your DNS settings to point to Vercel

## 🔒 Security Notes

- Never commit your production SECRET_KEY to version control
- Keep DEBUG=False in production
- Use HTTPS for all production traffic
- Consider using a managed database service (PostgreSQL)

## 📊 Monitoring

- Check Vercel dashboard for deployment status
- Monitor function execution times
- Review error logs regularly

---

**Need help?** Check the [Vercel documentation](https://vercel.com/docs) or [Django deployment guide](https://docs.djangoproject.com/en/stable/howto/deployment/).
