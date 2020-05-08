from django.contrib import admin
from django.urls import path, include

from .views import UserDetialAPIView, UserStatusAPIView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('<username>/', UserDetialAPIView.as_view(), name='detail'),
    path('<username>/status/', UserStatusAPIView.as_view(), name='status-list'),
]
