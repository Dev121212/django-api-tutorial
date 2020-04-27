from django.contrib import admin
from django.urls import path, include

from .views import AuthView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('', AuthView.as_view()),
    path('jwt/', obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token),
]
