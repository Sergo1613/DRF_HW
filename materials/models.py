from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.TextField(max_length=50, verbose_name='название курса')
    preview = models.ImageField(upload_to='preview/', verbose_name='превью курса', **NULLABLE)
    description = models.TextField(verbose_name='описание курса')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='courses', default=None, **NULLABLE)

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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='lessons', default=None, **NULLABLE)

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return f'{self.name}'