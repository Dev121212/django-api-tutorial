from rest_framework import pagination


# PageNumberPagination):
class TESTAPIPagination(pagination.LimitOffsetPagination):
    page_size = 5
    # max_limit = 3
