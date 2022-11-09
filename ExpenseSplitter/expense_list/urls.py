from django.urls import path
from .views import ExpenseList

urlpatterns = [
    path('', ExpenseList.as_view(), name='expenselist')
]