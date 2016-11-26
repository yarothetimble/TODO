from django.conf.urls import url

from . import views

app_name = 'tasks'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail' ),
    url(r'^add/$', views.TaskAdd.as_view(), name='task_add'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.TaskUpdate.as_view(), name='task_update'),
    #url(r'^(?P<pk>[0-9]+)/delete/$', views.TaskDelete.as_view(), name='task_delete'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]