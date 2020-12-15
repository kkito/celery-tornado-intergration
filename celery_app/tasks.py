from celery_app import celery_app

@celery_app.task
def demo_celery_run():
    return 'result is ok'