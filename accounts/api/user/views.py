from status.api.serializers import StatusInlineUserSerializer
from status.models import Status
from accounts.api.permissions import AnonPermission
from .serializers import UserDetailSerializer
from django.contrib.auth import get_user_model
from status.api.views import StatusAPIView
from rest_framework import(
    generics,
    permissions,
    # pagination,
)
from rest_framework.response import Response


User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}

# * Applying pagination in a single list view
# class TESTAPIPagination(pagination.PageNumberPagination):
#     page_size = 5


class UserStatusAPIView(StatusAPIView):
    serializer_class = StatusInlineUserSerializer
    # pagination_class = TESTAPIPagination

    def get_queryset(self, *srgs, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)


# class UserStatusAPIView(generics.ListAPIView):
#     serializer_class = StatusInlineUserSerializer
#     # pagination_class = TESTAPIPagination

#     def get_queryset(self, *srgs, **kwargs):
#         username = self.kwargs.get("username", None)
#         if username is None:
#             return Status.objects.none()
#         return Status.objects.filter(user__username=username)
