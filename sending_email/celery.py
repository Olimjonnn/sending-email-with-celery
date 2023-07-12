from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sending_email.settings')
app = Celery("sending_email", broker="redis://localhost:6379/1")

app.conf.enable_utc = False
app.conf.update(timezone='Asia/Tashkent')
app.config_from_object('django.conf:settings', namespace='CELERY')



app.conf.beat_schedule = {
    'send-email-every-1-minute': {
        'task': 'main.tasks.send_mail_func',
        'schedule': crontab(minute='*/1'),
        

    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')