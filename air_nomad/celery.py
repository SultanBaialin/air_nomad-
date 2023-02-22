import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'air_nomad.settings')

app = Celery('air_nomad')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-spam-every-30-seconds': {
        'task': 'air_nomad.tasks.send_spam_email',
        'schedule': 30.0
    }
}
