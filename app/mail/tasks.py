from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from api.services import get_statistic


@shared_task
def send_mail_task():
    for user in User.objects.all():
        subject = f"Statistic for {user.first_name} {user.last_name}"
        message = str(get_statistic(user))
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])
    return "Mails has been sent"