from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Category(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.title


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null= False, blank=False, default='title')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=False, blank=True, default='text')
    date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.amount} {self.user}'

    class Meta:
        ordering = ['-date']

