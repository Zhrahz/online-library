import django_filters
from apps.book.models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    # field2 = django_filters.NumberFilter(lookup_expr='gt')برای فیلد عددی به کار می رود

    class Meta:
        model = Book
        fields = ['title', 'author']
