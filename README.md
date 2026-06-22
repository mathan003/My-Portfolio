# Mathan Django Portfolio

A responsive Django portfolio inspired by the supplied reference layout, but rebuilt with original HTML/CSS/JS and content for Mathan M - Web Developer.

## Features
- Responsive single-page portfolio
- Hero, services, about, skills, projects, education/work and contact sections
- Django admin to add Services, Skills and Projects
- Contact form that stores messages in the SQLite database
- Original CSS portfolio visual (no external image dependency)

## Run locally (Windows / VS Code)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

Admin: `http://127.0.0.1:8000/admin/`

## Customize
- Edit your text in `portfolio/templates/portfolio/home.html`
- Change styling in `portfolio/static/portfolio/css/style.css`
- Add projects/services/skills in Django Admin
- Replace phone number and email in the Contact section

## Deployment reminders
Before deployment, set `DEBUG=False`, a real `SECRET_KEY`, production `ALLOWED_HOSTS`, a production database and static-file configuration.
