from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

app = Celery('web')
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()
