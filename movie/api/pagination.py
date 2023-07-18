from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size = 1


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'start'


class WatchListCPagination(CursorPagination):
    page_size = 1
    ordering = 'created'


