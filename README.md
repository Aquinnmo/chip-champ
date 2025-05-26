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

## Credits

[Adam Montgomery](adam-montgomery.ca)