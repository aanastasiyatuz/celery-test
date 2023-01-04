import os
from celery import Celery
from .settings import TIME_ZONE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.timezone = TIME_ZONE

app.autodiscover_tasks()

# python -m celery -A config worker -l info
