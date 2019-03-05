from django import forms
import django_filters
from .models import StoreItem


class StoreItemFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Price: Ascending'),
        ('descending', 'Price: Descending'),
    )

    ordering = django_filters.ChoiceFilter(
        label='Order by ', choices=CHOICES, method='filter_by_ordering')

    class Meta:
        model = StoreItem
        fields = {
            'name': ['icontains'],
            'code': ['icontains']
        }

    def filter_by_ordering(self, queryset, name, value):
        expression = 'price' if value == 'ascending' else '-price'
        return queryset.order_by(expression)
