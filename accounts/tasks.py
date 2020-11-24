from banksystem import celery_app
from .imports import *
# CODE Below


@celery_app.task(queue="priority_high")
def sendEmail(receipients:list, template_name:str, SENDER:str=settings.DEFAULT_EMAIL_SENDER, context:dict=None, attachments:dict=None):
    if not isinstance(receipients, list):
        receipients = [receipients]
    postoffice_mail.send(
        receipients,
        SENDER,
        template_name,
        context,
        attachments
    )