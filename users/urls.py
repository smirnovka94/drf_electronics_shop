from django.urls import path

from users.apps import UsersConfig
from users.views import UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView

app_name = UsersConfig.name
urlpatterns = [
    path('', UserListAPIView.as_view(), name='users_list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='users_update'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='users_view'),
]