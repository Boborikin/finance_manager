from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app')
app.conf.enable_utc=False
app.conf.update(timezone='Europe/Minsk')
app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
'Send_statistic_to_user': {
'task': 'mail.tasks.send_mail_task',
'schedule': crontab(hour=9),
}
}

app.autodiscover_tasks()