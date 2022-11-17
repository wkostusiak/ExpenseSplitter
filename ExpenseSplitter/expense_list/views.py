from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Expense
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils import timezone

class ExpenseLogin (LoginView):
    template_name = 'expense_list/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('expenselist')

class RegisterPage(FormView):
    template_name = 'expense_list/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('expenselist')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('expenselist')
        return super(RegisterPage, self).get(*args, **kwargs)

class ExpenseList(LoginRequiredMixin, ListView):
    model = Expense
    context_object_name = 'expenses'


class ExpenseDetail(LoginRequiredMixin, DetailView):
    model = Expense
    context_object_name = 'expense'


class ExpenseCreate(LoginRequiredMixin, CreateView):
    model = Expense
    fields = ['title', 'amount', 'description', 'category', 'date']
    success_url = reverse_lazy('expenselist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ExpenseCreate, self).form_valid(form)


class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = ['title', 'amount', 'description', 'category']
    success_url = reverse_lazy('expenselist')


class ExpenseDelete(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy('expenselist')


def totalsummary(request):
    User = get_user_model()
    receivers = User.objects.all()
    this_month = timezone.now().month
    context = {}
    total = {}
    for name in receivers:
        expense_total = Expense.objects.filter(date__month=this_month, user = name).aggregate(expenses=Sum('amount'))
        context[name] = (expense_total['expenses'])
        total[expense_total['expenses']] = name
        total_list = []
        for key in total.keys():
            key = float(key)
            total_list.append(key)
    return render(request, 'expense_list/summary.html', {'results': context, 'totals':total, 'total_list': total_list})



