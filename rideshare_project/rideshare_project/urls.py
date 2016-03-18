from django.conf.urls import patterns, include, url
from django.contrib import admin
from rideshare import views

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
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rideshare/', include('rideshare.urls')),
	url(r'^search_ride', views.search_ride, name='search_ride'),
	url(r'^post_ride', views.post_ride, name='post_ride'),
)
