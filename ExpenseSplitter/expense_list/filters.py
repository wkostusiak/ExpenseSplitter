import django_filters
from .models import Expense
from django_filters import DateFilter, CharFilter

class ExpenseFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr="gte", initial="dd/mm/yyyy")
    end_date = DateFilter(field_name="date", lookup_expr="lte", initial="dd/mm/yyyy")
    title = CharFilter(field_name="title", lookup_expr="icontains", initial="title")

    class Meta:
        model = Expense
        fields = ['user', 'category', 'title']
