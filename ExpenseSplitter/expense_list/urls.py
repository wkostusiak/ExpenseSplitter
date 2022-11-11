from django.urls import path
from .views import ExpenseList, ExpenseDetail, ExpenseCreate, ExpenseUpdate, ExpenseDelete

urlpatterns = [
    path('', ExpenseList.as_view(), name='expenselist'),
    path('expense/<int:pk>', ExpenseDetail.as_view(), name='expensedetail'),
    path('expense-create/', ExpenseCreate.as_view(), name='expensecreate'),
    path('expense-update/<int:pk>', ExpenseUpdate.as_view(), name='expenseupdate'),
    path('expense-delete/<int:pk>', ExpenseDelete.as_view(), name='expensedelete'),
]