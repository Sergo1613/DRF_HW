from celery import shared_task
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import timedelta


@shared_task()
def check_last_data():
    User = get_user_model()
    deadline_data = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=deadline_data, is_active=True)
    inactive_users.update(is_active=False)
    print(f'Deactivated {inactive_users.count()} users')
