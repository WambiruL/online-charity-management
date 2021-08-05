import django_filters

from .models import Category
class NGOFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name']