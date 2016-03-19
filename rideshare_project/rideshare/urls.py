from django.conf.urls import patterns, url
from rideshare import views

urlpatterns = patterns('',
        url(r'^$', views.main, name='main'),
	url(r'^login', views.login, name='login'),
	url(r'^register', views.register, name='register'),
	url(r'^post_ride', views.post_ride, name='post_ride'),
	url(r'^profile', views.profile, name='profile'),
)
