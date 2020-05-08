from django.contrib import admin
from django.urls import path, include

from .views import UserDetailAPIView, UserStatusAPIView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('<username>/', UserDetailAPIView.as_view(), name='detail'),
    path('<username>/status/', UserStatusAPIView.as_view()),
]
