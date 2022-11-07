from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from api.services import get_statistic


@shared_task
def send_mail_task():
    print("Mail sending.......")
    for user in User.objects.all():
        subject = f"Statistic for {user.first_name} {user.last_name}"
        message = str(get_statistic(user))
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, email_from, recipient_list)
    return "Mails has been sent........"