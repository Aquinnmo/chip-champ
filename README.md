# Project Noble

## About the Project

This project is aiming to provide a virtual alternative to physical poker chips for in-person Texas Hold Em games. Users will be able to all join a game lobby on each of their devices seperately and the service will handle all of their chips, side pots, and winnings virtually. The card game will still be performed in person, but with users using their device as a chip management system.

This service is aiming to make poker more accessible to all.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment file:
Copy `.env.example` to `.env` and update the values as needed.

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Dev Notes:

 - if adding a new static file, you must run one of the commands from `python manage.py collectstatic --help` if not done automatically, should be the command `python manage.py collectstatic --noinput`

## Project Structure

- `myproject/` - Main Django project settings
- `home/` - Home app with the main pages
- `templates/` - HTML templates
- `static/` - CSS, JS, and image files

## PLEASE NOTE

This service will handle NO ACTUAL TRANSFERS OF MONEY!!! It will aim to show each user how much they owe the pot/have won by the time they decide to leave the game.

## Deployment to Vercel

This project is configured for deployment to Vercel. Follow these steps:

### Prerequisites
1. Have a [Vercel account](https://vercel.com/)
2. Install the Vercel CLI: `npm i -g vercel`

### Deployment Steps

1. **Push your code to GitHub/GitLab/Bitbucket**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Connect to Vercel**
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "New Project"
   - Import your repository

3. **Environment Variables**
   Set these environment variables in your Vercel project settings:
   ```
   SECRET_KEY=your-production-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=.vercel.app,your-custom-domain.com
   DATABASE_URL=your-database-url (optional, uses SQLite by default)
   ```

4. **Deploy**
   - Vercel will automatically build and deploy your project
   - Your app will be available at `https://your-project-name.vercel.app`

### Local Testing for Production

To test production settings locally:
```bash
# Create a .env file with production settings
echo "DEBUG=False" > .env
echo "SECRET_KEY=your-secret-key" >> .env
echo "ALLOWED_HOSTS=localhost,127.0.0.1,.vercel.app" >> .env

# Run with production settings
python manage.py collectstatic --noinput
python manage.py runserver
```

### Important Notes for Vercel

- **Static Files**: The project uses WhiteNoise for serving static files
- **Database**: Uses SQLite by default. For production, consider using a hosted database service
- **Build Process**: Vercel runs `build_files.sh` to collect static files during deployment
- **WSGI**: Uses `vercel_app.py` as the WSGI entry point for Vercel

## Credits

[Adam Montgomery](adam-montgomery.ca)