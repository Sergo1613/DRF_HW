from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, CourseSubscription
from materials.paginators import CoursePaginator, LessonPaginator
from materials.permissions import IsOwner, IsModerator
from materials.serializers import CourseSerializer, LessonSerializer, CourseSubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    pagination_class = CoursePaginator

    def create(self, request, *args, **kwargs):
        # Checking if a user is a moderator
        is_moderator = request.user.groups.filter(name='Moderators').exists()
        if is_moderator:
            return self.permission_denied(request)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Checking if a user is a moderator
        is_moderator = request.user.groups.filter(name='Moderators').exists()
        if is_moderator:
            return self.permission_denied(request)
        return super().destroy(request, *args, **kwargs)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class CourseSubscriptionAPIView(APIView):
    def get(self, request):
        user = request.user

        # Получение всех подписок для текущего пользователя
        subscriptions = CourseSubscription.objects.filter(user=user)

        # Сериализация подписок
        subscription_serializer = CourseSubscriptionSerializer(subscriptions, many=True)

        # Получение всех курсов
        courses = Course.objects.all()

        # Сериализуем курсы, передавая подписки в контекст
        course_serializer = CourseSerializer(courses, many=True, context={'request': request})

        # Возврат JSON с данными о курсах и подписках
        return Response({"courses": course_serializer.data, "subscriptions": subscription_serializer.data},
                        status=status.HTTP_200_OK)

        # Проверка подлинности пользователя
        if user.is_authenticated:
            # Получение всех подписок текущего пользователя
            subscriptions = CourseSubscription.objects.filter(user=user)
            serializer = CourseSubscriptionSerializer(subscriptions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Возвращать сообщение об ошибке, если пользователь не аутентифицирован
            return Response({"message": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, course_id):
        user = request.user

        # Проверка подлинности пользователя
        if user.is_authenticated:
            # Получение объекта курса из базы данных с помощью get_object_or_404
            course = get_object_or_404(Course, id=course_id)

            # Получение объектов подписки по текущему пользователю и тарифу
            subscription, created = CourseSubscription.objects.get_or_create(user=user, course=course)

            if created:
                message = 'Subscription has been created successfully.'
            else:
                subscription.delete()
                message = 'Subscription  has been deleted successfully.'

            serializer = CourseSubscriptionSerializer(subscription)
            return Response({"message": message, "subscription": serializer.data}, status=status.HTTP_200_OK)
        else:
            # Возвращать сообщение об ошибке, если пользователь не аутентифицирован
            return Response({"message": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
