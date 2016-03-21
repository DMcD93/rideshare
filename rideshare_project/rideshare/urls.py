from django.conf.urls import patterns, include, url
from rideshare import views

urlpatterns = patterns('',
    url(r'^', views.search_ride, name='search_ride'),
	url(r'^(?P<journey>\d+)/$', views.bookSeat, name='bookSeat'),
)
