# Django Project

A Django web application template with multiple pages support.

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

## Project Structure

- `myproject/` - Main Django project settings
- `home/` - Home app with the main pages
- `templates/` - HTML templates
- `static/` - CSS, JS, and image files
