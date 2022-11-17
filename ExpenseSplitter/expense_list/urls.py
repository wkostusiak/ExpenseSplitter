from django.urls import path
from . import views
from .views import ExpenseList, ExpenseDetail, ExpenseCreate, ExpenseUpdate, ExpenseDelete, ExpenseLogin, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', ExpenseList.as_view(), name='expenselist'),
    path('login/', ExpenseLogin.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('expense/<int:pk>', ExpenseDetail.as_view(), name='expensedetail'),
    path('expense-create/', ExpenseCreate.as_view(), name='expensecreate'),
    path('expense-update/<int:pk>', ExpenseUpdate.as_view(), name='expenseupdate'),
    path('expense-delete/<int:pk>', ExpenseDelete.as_view(), name='expensedelete'),
    path('expense-summary/', views.totalsummary, name='expensesummary'),

]