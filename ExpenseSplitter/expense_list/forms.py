from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Register(UserCreationForm):
  email = forms.EmailField(required=True)

  def clean_email(self):
    email = self.cleaned_data.get('email', '')
    if User.objects.filter(email=email).exists():
      raise ValidationError("Email exists")

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
