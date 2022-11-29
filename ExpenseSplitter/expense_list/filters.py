import django_filters
from .models import Expense
from django_filters import CharFilter

class ExpenseFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Expense
        fields = ['category', 'user', 'date']
