# Starley Group Solutions

Website and web application for **Starley Group Solutions**, an IT company
delivering software development, cloud & DevOps, cybersecurity, IT consulting,
managed support and data analytics.

Built with Django, it is designed to be **modular and scalable** — new modules
(services, careers, case studies, portals, etc.) can be added without rewriting
the core infrastructure.

## Tech stack

- Django 5.2
- Tailwind CSS (classes are prefixed with `tw-`)
- SQLite for local development, PostgreSQL in production
- WhiteNoise for static files, Gunicorn for serving
- Deployable to Vercel / Railway / Render

## Project structure

```
project/            # settings, root urls, sitemaps, shared views (home, errors)
core/               # scalable foundation: abstract base models + context processor
user/               # custom user model & auth
blog/               # blog with WYSIWYG editor in the admin
inquiry/            # "Contact us" enquiries
services/           # IT service offerings (example content module)
styling/            # Tailwind app
templates/          # html / css / js / assets (images live here, untouched)
utils/              # shared helpers (validators, mailing, managers, etc.)
```

### The `core` app (why this is scalable)

`core` holds the infrastructure every module reuses, so modules stay thin and
consistent:

- `core.models.TimeStampedModel` / `PublishableModel` — abstract base models
  giving `created_at` / `updated_at` (and publish/ordering) to any model.
- `core.context_processors.site_context` — injects `company` details and the
  primary navigation (`nav_links`) into **every** template. Branding and the
  menu are configured once in `project/settings.py` (`COMPANY`, `NAV_LINKS`).

## Adding a new module (no core changes required)

The `services` app is a complete reference example. To add a module (e.g.
`careers`):

1. `python manage.py startapp careers`
2. In `careers/models.py`, inherit the shared base:
   ```python
   from core.models import TimeStampedModel

   class Job(TimeStampedModel):
       ...
   ```
3. Add `'careers'` to `LOCAL_APPS` in `project/settings.py`.
4. Create `careers/urls.py` and include it in `project/urls.py`:
   `path('careers/', include('careers.urls'))`.
5. (Optional) add a link to `NAV_LINKS` in settings — it appears in the header
   and footer automatically.
6. (Optional) add a `Sitemap` and register it in `project/urls.py`.
7. `python manage.py makemigrations && python manage.py migrate`.

No edits to `base.html`, the context processor or other modules are needed.

## Local development

1. Create and activate a virtual environment.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root (see `.env.local.example`). For a
   quick local start you only need:
   ```
   DEBUG=1
   SECRET_KEY="a-local-dev-secret-key"
   FIREBASE_CRED_PATH="project/firebase-cred.json"
   GOOGLE_ANALYTICS="G-XXXX"
   PROJECT_ID=""
   ```
4. Apply migrations (this also seeds the default services):
   ```
   python manage.py migrate
   ```
5. Run the server:
   ```
   python manage.py runserver
   ```
   Visit http://localhost:8000/
6. (Optional) run Tailwind in watch mode in a second terminal:
   ```
   python manage.py tailwind start
   ```

### Admin superuser

```
python manage.py createsuperuser
```

Manage services, blog posts and enquiries from the admin panel at `/admin/`.

## Deployment

Set `DEBUG=0`, provide a production `PORD_SECRET_KEY`, database (`POSTGRES_URL`)
and allowed hosts/CORS, then run:

```
python manage.py collectstatic --noinput
python manage.py migrate
```

`Procfile` and `vercel.json` are included for Railway/Render and Vercel.

## Credits

Bootstrapped from an open-source Django website template
([PaulleDemon/Django-website-template](https://github.com/PaulleDemon/Django-website-template));
see `readme.md` for the original template documentation. Images are placeholders
from free-to-use sources (Unsplash, Pexels).
