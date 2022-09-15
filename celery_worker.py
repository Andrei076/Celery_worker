import resize
from celery import Celery

app = Celery('celery_worker', broker='pyamqp://guest@localhost//')


@app.task
def task1(image_path):
    resize.resizer(image_path)
    return True
