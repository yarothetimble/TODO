from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('tasks:detail', kwargs={'pk' : self.pk})