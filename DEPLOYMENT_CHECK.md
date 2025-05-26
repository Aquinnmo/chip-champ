# Manual Deployment Check

## Quick Steps to Verify Your Deployment

### 1. Find Your Deployment URL
- Go to your Vercel dashboard (https://vercel.com/dashboard)
- Find your project and click on it
- Copy the deployment URL (e.g., https://your-project.vercel.app)

### 2. Check if the Site Loads
- Open your deployment URL in a browser
- The page should load without errors

### 3. Check Browser Developer Tools
- Press F12 to open developer tools
- Go to the "Network" tab
- Reload the page (F5)
- Look for these files and their status:
  - `/static/css/style.css` - Should be Status 200 (green)
  - `/static/images/cc_logo.png` - Should be Status 200 (green)
  - `/static/js/main.js` - Should be Status 200 (green)

### 4. Visual Check
- Check if the site has proper styling (colors, fonts, layout)
- Check if the logo image appears in the navigation
- Check if the favicon appears in the browser tab

### 5. If Static Files Are Not Working

#### Ensure Static Files Are Collected Before Deploying
- The build process must run `python manage.py collectstatic --noinput` to copy static files into the `staticfiles/` directory.
- This is handled automatically by the `build_files.sh` script during Vercel deployment.
- If you add or change static files, always redeploy so the latest files are collected.

#### Option A: Redeploy (Recommended)
1. Commit your changes: `git add . && git commit -m "Fix static files configuration"`
2. Push to your repository: `git push`
3. Vercel will automatically redeploy

#### Option B: Manual Redeploy
If you have Vercel CLI installed:
```bash
vercel --prod
```

### 6. Common Issues and Solutions

**If CSS is not loading:**
- Check that `/static/css/style.css` returns Status 200 in browser dev tools
- If it returns 404, the static files routing or collection is not working

**If images are not loading:**
- Check that `/static/images/cc_logo.png` returns Status 200
- If 404, same routing or collection issue

**If nothing is styled:**
- Check that the CSS file content is correct (not empty or error page)
- View source of your page and make sure it contains: `<link rel="stylesheet" href="/static/css/style.css">`

### 7. Test with Python Script
Run this command and enter your deployment URL when prompted:
```bash
python test_deployment.py
```

This will automatically test all static files and report any issues.
