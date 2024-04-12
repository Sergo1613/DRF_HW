from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, CourseSubscriptionAPIView, CoursePaymentApiView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('subscription/<int:course_id>/', CourseSubscriptionAPIView.as_view(), name='course-subscription'),
    path('subscription/', CourseSubscriptionAPIView.as_view(), name='list-subscription'),
    path('payment_course/create/', CoursePaymentApiView.as_view(), name='course-payment'),
] + router.urls
