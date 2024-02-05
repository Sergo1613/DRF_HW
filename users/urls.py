from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, PaymentsListApiView

app_name = UsersConfig.name

urlpatterns = [
    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-get'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
    path('payments/', PaymentsListApiView.as_view(), name='payments_list'),
]
