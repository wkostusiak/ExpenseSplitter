import django_filters
from .models import Expense, Category
from django_filters import CharFilter, DateFromToRangeFilter, ModelChoiceFilter
from django_filters.widgets import RangeWidget
from django.forms.widgets import TextInput


class ExpenseFilter(django_filters.FilterSet):
    date = DateFromToRangeFilter(field_name="date", widget=RangeWidget(attrs={'placeholder': 'dd/mm/yyyy'}))
    title = CharFilter(field_name="title", lookup_expr="icontains", widget=TextInput(attrs={'placeholder': 'enter text here'}))
    category = ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Expense
        fields = []