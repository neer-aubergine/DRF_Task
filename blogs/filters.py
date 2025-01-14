from django_filters import rest_framework as filters
from .models import Blog

class BlogFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author__username', lookup_expr='icontains')
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    tags = filters.CharFilter(method='filter_by_tags')

    class Meta:
        model = Blog
        fields = ['author', 'category', 'tags']

    def filter_by_tags(self, queryset, name, value):
        tag_names = value.split(',')
        return queryset.filter(tags__name__in=tag_names).distinct()