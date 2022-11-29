from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Expense
from django.db.models import Sum
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .filters import ExpenseFilter





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

    def get_queryset(self):
        qs = self.model.objects.all()
        product_filtered_list = ExpenseFilter(self.request.GET, queryset=qs)
        return product_filtered_list.qs

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
    q = request.GET["q"]
    if q:
        User = get_user_model()
        receivers = User.objects.all()
        total = {}
        x = 0 #number of users to split expenses#
        for name in receivers:
            expense_total = Expense.objects.filter(user = name, date__month=q).aggregate(expenses = (Sum('amount')))
            if expense_total == {'expenses':None}:
                total[name] = 0
            else:
                total[name] = expense_total['expenses']

            x += 1
            total_list = []
            people_list = []
            for key in total.keys():
                key = str(key)
                people_list.append(key)
            for value in total.values():
                name = float(value)/x
                total_list.append(name)
            dic = dict(zip(people_list,total_list))
            t = 0  # t is for controlling while loop#
            n = len(dic)
            users = people_list
            val = total_list
            splitted = []
            while t < len(dic):
                i = 0  # main user - counting money for this person#
                k = 1  # k is for while loop and indexing other users#
                while k <= (n - 1):
                    if val[i] < val[i + k]:
                        splitted.append(f" {users[i]} owes {users[i + k]} {(val[i + k] - val[i]):.2f}")
                    if val[i] > val[i + k]:
                        splitted.append(f" {users[i + k]} owes {users[i]} {(val[i] - val[i + k]):.2f}")
                    if val[i] == val[i + k]:
                        splitted.append(f" {users[i]} and {users[i + k]} are equal")
                    k += 1
                users = users[1:]  # getting rid of the main user I am done with#
                val = val[1:]  # getting rid of the main user I am done with#
                t += 1
                n = n - 1  # n updating, because in each step we need less iteration in second loop - less users left#
    else:
        return redirect('expense_list/expense_list.html')
    return render(request, 'expense_list/summary.html', {'results': total.keys(), 'totals':total.values(), 'total_list': total_list, 'people_list' : people_list, 'splitted':splitted})



