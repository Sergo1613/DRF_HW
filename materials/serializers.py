from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    # Создание поля для подсчета уроков
    lessons_count = serializers.SerializerMethodField()

    # Создание списка уроков для курса
    lessons_list = LessonSerializer(many=True, source='lessons')

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, objects):
        return objects.lessons.count()


