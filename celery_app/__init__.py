from celery import Celery

task_list = [
    'celery_app.tasks'
]

celery_app = Celery("testTornadoCelery")
celery_app.config_from_object('celery_app.config')
celery_app.autodiscover_tasks(task_list)