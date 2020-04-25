from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer


class StatusListSearchAPIView(APIView):  # Making our own view
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

# CreateModelMixin handles post data
# UpdateModelMixin handles put data


class StatusAPIView(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.ListAPIView):

    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id', None)
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
'''
All three Retrieve, Update, Destroy at once place
'''
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


class StatusDetailAPIView(generics.RetrieveAPIView,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.UpdateModelMixin,):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # * If your passing the arguement 'id' in the path the 'lookup_field' is required.
    # * Otherwise in path write '<pk>'
    # lookup_field = 'id'

    # * If you don't want to use 'lookup_field' and have passed 'id' in path, then use this function
    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)


class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
