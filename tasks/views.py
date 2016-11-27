from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import View

from .forms import LoginForm
from .forms import TaskForm
from .forms import RegisterForm
from .models import Task

class IndexView(LoginRequiredMixin, generic.ListView):
	template_name = 'tasks/index.html'
	login_url = '/tasks/login/'

	def get_queryset(self):
		return Task.objects.filter(user=self.request.user)

	def get_user(self):
		return queryset.get(user=self.request.user)

class DetailView(LoginRequiredMixin, generic.DetailView):
	model = Task
	login_url = '/tasks/login/'
	template_name = 'tasks/detail.html'

	def get(self, request, pk):
		#import ipdb;ipdb.set_trace()
		task = get_object_or_404(Task, pk=pk, user=self.request.user)
		return render(request, self.template_name, {'task' : task})

	def post(self, request, *args, **kwargs):
		if "update" in request.POST:
			return HttpResponseRedirect('/tasks/' + str(kwargs['pk']) + '/update')
		elif "delete" in request.POST:
			task = get_object_or_404(Task, pk=kwargs['pk'], user=self.request.user)
			task.delete()
			return redirect('tasks:index')# + str(kwargs['pk']) + '/delete')

class TaskAdd(LoginRequiredMixin, CreateView):
	model = Task
	login_url = '/tasks/login/'
	fields = ['title', 'description']

	def form_valid(self, form):
		task = form.save(commit=False)
		task.user = self.request.user
		task.save()
		return redirect(task.get_absolute_url())

class TaskUpdate(LoginRequiredMixin, View):
	form_class = TaskForm
	login_url = '/tasks/login/'
	template_name = 'tasks/task_form.html'

	def get(self, request, pk):
		task = Task.objects.get(pk=pk)
		form = self.form_class(instance=task)
		return render(request, self.template_name, {'form' : form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			get_object_or_404(Task, pk=kwargs['pk'], user=self.request.user)
			task = form.save(commit=False)
			task.user = request.user
			task.id = kwargs['pk']
			task.save()
			return HttpResponseRedirect('/tasks/' + str(kwargs['pk']))
		return render(request, self.template_name, {'form' : form}) 

class LoginView(View):
	form_class = LoginForm
	template_name = 'tasks/login.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form' : form})

	def post(self, request):
		form = self.form_class(request.POST)

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('tasks:index')

		return render(request, self.template_name, {'form' : form})

def logout_view(request):
	logout(request)
	return redirect('tasks:login')

class RegisterView(View):
	form_class = RegisterForm
	template_name = 'tasks/register.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form' : form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('tasks:index')

		return render(request, self.template_name, {'form' : form})