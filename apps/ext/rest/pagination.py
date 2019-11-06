from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'size'
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'size'
    max_page_size = 100


class NormalPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'
    max_page_size = 100
