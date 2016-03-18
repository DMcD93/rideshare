from django.conf.urls import patterns, include, url
from rideshare import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^registration/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
)
