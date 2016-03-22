import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rideshare_project.settings")

import django
django.setup()
from django.utils import timezone

from rideshare.models import Review
from django.contrib.auth.models import User

def populate():
	user_one = add_user(username='Harry',
	password='harry',
	email='harry@abc.com',
	first_name='Harry',
	last_name='Potter')
	
	add_review(user=user_one,
	description='This should work!!',
	posted_by='monica',
	posted_at=timezone.now())
	
	add_review(user=user_one,
	description='This better work.',
	posted_by='Sally',
	posted_at=timezone.now())
	
def add_user(username, password, email, first_name, last_name):
	#b= User.objects.get_or_create(username=username, password=password, email=email, first_name=first_name,last_name=last_name)[0]
	#b.save()
	#return b
	
	b=User.objects.get_or_create(username=username)[0]
	b.set_password(password)
	b.email=email
	b.first_name=first_name
	b.last_name=last_name
	b.save()
	return b
	
def add_review(user, description, posted_by, posted_at):
	a = Review.objects.get_or_create(user=user, posted_at=posted_at)[0]
	#a.phone=phone
	a.description=description
	a.posted_at=posted_at
	a.posted_by=posted_by
	a.save()
	return a
	
if __name__ == '__main__':
	print "Starting population script"
	populate()