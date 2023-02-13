from .celery import app
from django.core.mail import send_mail

from account.send_mail import send_confirmation_email, send_notification


@app.task
def send_confirmation_tasks_email(user, code):
    send_confirmation_email(user=user, code=code)


def send_notification_task(user_email, order_id, price):
    send_notification(user_email, order_id, price)
