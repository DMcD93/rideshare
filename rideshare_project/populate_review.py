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
	description='Good driver!!!',
	posted_by='Sally',
	posted_at=timezone.now())
	
	add_review(user=user_one,
	description='Leifos is better!',
	posted_by='laura',
	posted_at=timezone.now())
	
	user_two = add_user(username='leifos',
	password='leifos',
	email='leifos@awesome.com',
	first_name='Leif',
	last_name='Azzopardi')
	
	add_review(user=user_two,
	description='Awesome guy with a sweet ride.',
	posted_by='david',
	posted_at=timezone.now())
	
	add_review(user=user_two,
	description='No.1',
	posted_by='Laura',
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