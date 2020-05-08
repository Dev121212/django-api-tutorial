from rest_framework import pagination


# PageNumberPagination):
class TESTAPIPagination(pagination.LimitOffsetPagination):
    max_limit = 3
