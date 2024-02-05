from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils import timezone

from materials.models import Course, Lesson
from users.models import Payments

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Создание тестового пользователя
        user = User.objects.create(username='sergo29', first_name='Sergey', last_name='Telkin', email='sergey29@example.com')

        # Создание тестового курса
        course = Course.objects.create(name='backend', description='this is the backend course')

        # Создание тестового урока
        lesson = Lesson.objects.create(name='lesson_C++', description='this is the lesson_C++', course=course)

        # Создание тестовой оплаты
        payment = Payments.objects.create(
            user=user,
            date_of_payment=timezone.now(),
            paid_course=course,
            paid_lesson=lesson,
            payment_amount=220.10,
            payment_method='transfer'
        )

        self.stdout.write(self.style.SUCCESS('Successfully created sample payments'))
