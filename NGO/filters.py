import django_filters

from .models import Category,NGO
class NGOFilter(django_filters.FilterSet):
    name= NGO.objects.all()
    class Meta:
        model =NGO
        fields = ['category__name']