# Copilot Instructions for xPack Application

## Project Overview
- This is a multi-app Django project for package registry and device management.
- Main apps: `xPack_App` (dashboard, device registry, admin views), `xPack_Registrar` (registrar and family management).
- Data flows between apps via shared models and cross-app imports (e.g., `from xPack_Registrar.models import Registry`).
- Static assets are in `/static/` and templates in `/templates/`, organized by feature.

## Architecture & Patterns
- Each app has its own `models.py`, `views.py`, `forms.py`, `urls.py`, and `migrations/`.
- Cross-app model usage is common (see dashboard views importing `Registry` from registrar).
- Templates are grouped by feature (e.g., `dashboard/`, `registrar/`).
- Static files (CSS, JS, images) are referenced using `{% load static %}` and `{% static '...' %}`.
- Database: PostgreSQL (Supabase) is used; credentials are set directly in `settings.py`.
- Custom admin/dashboard logic in `xPack_App/views.py` and `xPack_Registrar/views.py`.
- Authentication handled through Django's built-in auth system.

## Developer Workflows
- Run server: `python manage.py runserver`
- Migrate DB: `python manage.py makemigrations && python manage.py migrate`
- Test: `python manage.py test xPack_App` or `python manage.py test xPack_Registrar`
- Static files: Place in `/static/`, reference in templates, run `python manage.py collectstatic` for deployment.
- Debug: Use Django's built-in error pages and messages framework (`django.contrib.messages`).
- Virtual Environment: Use `xenv` for dependency isolation.

## Conventions & Integration
- All Django forms are in `forms.py` per app; use ModelForm for CRUD.
- Views use explicit imports for cross-app models (not Django's `apps.get_model`).
- URL routing: Each app has its own `urls.py`, included in the main project's `urls.py`.
- Supabase integration: Database settings are hardcoded; update `settings.py` for new credentials.
- No custom management commands or Celery tasks detected.
- Form validation messages use Django's messages framework.
- Model relationships follow Django's standard foreign key conventions.

## Deployment Guidelines
- Production settings should be in separate `settings_prod.py`
- Use environment variables for sensitive data
- Run `python manage.py check --deploy` before deployment
- Ensure DEBUG=False in production
- Configure ALLOWED_HOSTS appropriately
- Run `python manage.py collectstatic` for static files
- Use proper WSGI/ASGI server (e.g., Gunicorn)
- Set up proper database backup strategy

## Security Practices
- Never commit sensitive data to version control
- Use Django's built-in XSS protection
- Enable CSRF protection on all forms
- Use secure session configuration
- Implement proper user authentication
- Regular security updates for dependencies
- Input validation on all form submissions
- Proper error handling to prevent information leakage

## Testing Strategy
- Unit tests for models in each app's `tests.py`
- Integration tests for views and forms
- Test database uses SQLite by default
- Coverage reporting recommended
- Test all form validations
- Test authentication/authorization
- Test cross-app model relationships
- Mock external services (Supabase) in tests

## Examples
- To add a new dashboard view, create a function in `xPack_App/views.py`, add template in `templates/dashboard/`, and update `xPack_App/urls.py`.
- To add a new model, define in `models.py`, run migrations, and update forms/views/templates as needed.
- To add family member: Use `FamilyForm` in views, template in `registrar/family_entry.html`
- To track package actions: Use `PackageAction` model with Registry relationship

## Key Files & Directories
- `xPack/settings.py`: Django settings, DB config
- `xPack_App/views.py`, `xPack_Registrar/views.py`: Main business logic
- `xPack_App/models.py`, `xPack_Registrar/models.py`: Data models
- `static/`: All static assets
- `templates/`: All HTML templates
- `xenv/`: Virtual environment
- `migrations/`: Database schema changes

## Troubleshooting
- Check Django debug page for detailed error traces
- Verify database connectivity in Django admin
- Check migration history if model changes not reflecting
- Review logs for background task issues
- Ensure proper template context in views
- Verify form validation messages
- Check static file paths and collectstatic status
- Monitor database query performance

## Models Reference
### Registry Model
- Tracks package registrations
- Related to PackageAction for status tracking
- Can have multiple family members (Family model)

### Family Model
- Represents family members
- Links to Registry through foreign key
- Used in family management views

### PackageAction Model
- Tracks package status changes
- Links to Registry through foreign key
- Used in served/rejected package views

---
_If any conventions or workflows are unclear, please provide feedback so this guide can be improved._
