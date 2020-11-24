from banksystem import celery_app

# CODE Below
@celery_app.task
def summer(a,b):
    return a+b