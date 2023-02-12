from .celery import app
from django.core.mail import send_mail

from account.send_mail import send_confirmation_email


@app.task
def send_confirmation_tasks_email(user, code):
    send_confirmation_email(user=user, code=code)


