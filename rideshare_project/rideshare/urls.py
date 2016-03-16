from django.conf.urls import patterns, include, url
from rideshare import views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
	url(r'^login', views.login, name='login'),
	url(r'^register', views.register, name='register'),
	url(r'^post_ride', views.post_ride, name='post_ride'),
	url(r'^admin/', include(admin.site.urls))
)
