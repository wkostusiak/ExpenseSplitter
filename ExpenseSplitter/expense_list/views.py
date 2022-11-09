from django.shortcuts import render
from django.views.generic import ListView
from .models import Expense


class ExpenseList(ListView):
    model = Expense
    context_object_name = 'expenses'



