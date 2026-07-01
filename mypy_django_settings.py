"""Settings minimale usato solo da django-stubs per il type-checking di baton.

Non e' un progetto Django reale: serve unicamente a far risolvere al plugin
django-stubs la configurazione dinamica di Django (modelli, campi, request...).
Il progetto di sviluppo/test vero e proprio resta la testapp/.
"""

SECRET_KEY = "type-checking-only"

STATIC_URL = "/static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "baton",
    "baton.autodiscover",
]
