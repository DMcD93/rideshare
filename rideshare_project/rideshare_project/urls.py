from django.conf.urls import patterns, include, url
from django.contrib import admin
from rideshare import views
from rideshare import urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rideshare_project.views.home', name='home'),
    # url(r'^rideshare_project/', include('rideshare_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^$', views.main, name='main'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^search_ride/', include('rideshare.urls', namespace="search")),
	url(r'^post_ride', views.post_ride, name='post_ride'),
	url(r'^add_vehicle', views.add_vehicle, name='add_vehicle'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^registration/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
)
