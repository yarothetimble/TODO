from django import forms
from django.contrib.auth.models import User

from .models import Task

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'password']

class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password'];

class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ['title', 'description', 'complete'];