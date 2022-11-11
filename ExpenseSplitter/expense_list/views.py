from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Expense
from django.urls import reverse_lazy


class ExpenseList(ListView):
    model = Expense
    context_object_name = 'expenses'


class ExpenseDetail(DetailView):
    model = Expense
    context_object_name = 'expense'


class ExpenseCreate(CreateView):
    model = Expense
    fields = ['title', 'amount', 'description', 'category','user']
    success_url = reverse_lazy('expenselist')


class ExpenseUpdate(UpdateView):
    model = Expense
    fields = ['title', 'amount', 'description', 'category', 'user']
    success_url = reverse_lazy('expenselist')


class ExpenseDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('expenselist')