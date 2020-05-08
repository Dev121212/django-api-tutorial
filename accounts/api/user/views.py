from .serializers import UserDetailSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from accounts.api.permissions import AnonPermission

from status.models import Status
from status.api.serializers import StatusInlineUserSerializer

User = get_user_model()


class UserDetialAPIView(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}


class UserStatusAPIView(generics.ListAPIView):
    serializer_class = StatusInlineUserSerializer

    def get_queryset(self, *srgs, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)
