import os

from celery import Celery

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
os.environ.setdefault("DJANGO_SETTINGS_MODULE","pickem.settings")




app = Celery('pickem',
             broker='amqp://rfheise:35134rfh@161.35.124.49:5672/vhost',
             backend='amqp://rfheise:35134rfh@161.35.124.49:5672/vhost',)

app.conf.beat_schedule = {
     'add-every-monday-morning': {
        'task': 'winem.tasks.message',
        'schedule': 30.0,
        'args': ("wow grape","+15742073299"),
    }
}

app.conf.timezone = 'America/Indianapolis'

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)
app.config_from_object('django.conf:settings', namespace='CELERY')
#gets all tasks from all the other apps installed under django settings
app.autodiscover_tasks()
if __name__ == '__main__':
    app.start()

@app.task
def message(body,to,from_="+19085214850"):
    client = Client(account_sid, auth_token)
    client.messages.create(body=body,from_=from_,to=to)
#used to tell you when a task is running
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
