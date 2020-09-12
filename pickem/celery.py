import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE","pickem.settings")


app = Celery("pickem")

app.config_from_object('django.conf:settings', namespace='CELERY')
#gets all tasks from all the other apps installed under django settings
app.autodiscover_tasks()

#used to tell you when a task is running
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
