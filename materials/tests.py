from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from materials.models import Course
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        # Создание пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.course = Course.objects.create(
            name='test',
            description='first course',
            owner=self.user
        )

    def test_get_lesson_authenticated(self):
        """ Получение курса уроков авторизованным пользователем."""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('materials:lesson-list')
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
