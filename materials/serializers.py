from rest_framework import serializers

from materials.models import Course, Lesson, CourseSubscription, CoursePayment
from materials.validators import validator_scam_url


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonCreateSerializer(serializers.ModelSerializer):

    video_link = serializers.URLField(validators=[validator_scam_url])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    is_subscribed = serializers.SerializerMethodField()

    # Создание поля для подсчета уроков
    lessons_count = serializers.SerializerMethodField()

    # Создание списка уроков для курса
    lessons_list = LessonSerializer(many=True, read_only=True, source='lessons')

    link_of_payment = serializers.URLField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribed(self, instance):
        # Получение текущего пользователя
        user = self.context['request'].user

        # Проверка подписки пользователя на этот курс
        if user.is_authenticated:
            return CourseSubscription.objects.filter(user=user, course=instance).exists()
        else:
            return False

    def get_lessons_count(self, objects):
        return objects.lessons.count()


class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = '__all__'


class CoursePaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoursePayment
        fields = '__all__'
