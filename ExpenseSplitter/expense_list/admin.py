from django.contrib import admin
from .models import Expense, Category

admin.site.register(Expense)
admin.site.register(Category)