from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from materials.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):

    MEMBER = 'member', _('member'),
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    phone = models.CharField(max_length=50, verbose_name='номер телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Payments(models.Model):

    PAYMENT_CHOICES = [
        ('transfer', 'transfer to account'),
        ('cash', 'cash'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date_of_payment = models.DateField(verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный урок')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_CHOICES, verbose_name='способ оплаты')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

    def __str__(self):
        return f'{self.user}'
