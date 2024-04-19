from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_mail_about_updates(recipient_email, course_title):
    send_mail(
        subject='course update notification',
        message=f"the course {course_title} has been updated. Check out the new materials!",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_email],
        fail_silently=False
    )
