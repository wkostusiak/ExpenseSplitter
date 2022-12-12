import django_filters
from .models import Expense, Category
from django_filters import DateFilter, CharFilter, ModelChoiceFilter
from django.db import models
from django.contrib.auth.models import User


class ExpenseFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr="gte", initial="dd/mm/yyyy")
    end_date = DateFilter(field_name="date", lookup_expr="lte", initial="dd/mm/yyyy")
    title = CharFilter(field_name="title", lookup_expr="icontains", initial="title")

    class Meta:
        model = Expense
        fields = []