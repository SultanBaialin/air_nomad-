from account.models import Spam_Contacts
from .celery import app
from django.core.mail import send_mail

from account.send_mail import send_confirmation_email, send_notification


@app.task
def send_confirmation_tasks_email(user, code):
    send_confirmation_email(user=user, code=code)


@app.task
def send_notification_task(user_email, order_id, price):
    send_notification(user_email, order_id, price)

@app.task
def send_spam_email():
    ls = [user.email for user in Spam_Contacts.objects.all()]
    send_mail(
        'SPAM SPAM SPAM',
        'THIS IS SPAM LETTER',
        'JOHNSNOW',
        [*ls],
        fail_silently=False
        )