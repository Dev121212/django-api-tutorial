from status.api.serializers import StatusInlineUserSerializer
from status.models import Status
from accounts.api.permissions import AnonPermission
from .serializers import UserDetailSerializer
from django.contrib.auth import get_user_model
from rest_framework import(
    generics,
    permissions,
    # pagination,
)


User = get_user_model()


class UserDetialAPIView(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}

# * Applying pagination in a single list view
# class TESTAPIPagination(pagination.PageNumberPagination):
#     page_size = 5


class UserStatusAPIView(generics.ListAPIView):
    serializer_class = StatusInlineUserSerializer
    # pagination_class = TESTAPIPagination

    def get_queryset(self, *srgs, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)
