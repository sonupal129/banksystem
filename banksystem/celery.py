import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banksystem.settings')


## Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('banksystem')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL


app.conf.beat_schedule = {
    'send-queued-mail': {
        'task': 'post_office.tasks.send_queued_mail',
        'schedule': 600.0,
    },
    'cleanup_mail': {
        'task': 'post_office.tasks.cleanup_mail',
        'schedule': 600.0, #TBD timeframe
    },
}
