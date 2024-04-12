from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.TextField(max_length=50, verbose_name='название курса')
    preview = models.ImageField(upload_to='preview/', verbose_name='превью курса', **NULLABLE)
    description = models.TextField(verbose_name='описание курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')
    url = models.URLField(verbose_name='url', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name='цена', **NULLABLE)


    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return f'{self.name}'


class Lesson(models.Model):
    name = models.TextField(max_length=50, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока', **NULLABLE)
    preview = models.ImageField(upload_to='preview/', verbose_name='превью урока', **NULLABLE)
    video_link = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, related_name='lessons')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='lessons', default=None, **NULLABLE)

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return f'{self.name}'


class CourseSubscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)


class CoursePayment(models.Model):
    price_amount = models.CharField(verbose_name='сумма оплаты')
    payment_link = models.URLField(max_length=400, verbose_name='ссылка на оплату', **NULLABLE)
    payment_id = models.CharField(max_length=255, verbose_name='id_of_payment', **NULLABLE)

    class Meta:
        verbose_name = 'оплата курса'
        verbose_name_plural = 'оплаты курсов'

    def __str__(self):
        return self.payment_id
