import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rideshare_project.settings")

import django
django.setup()
from django.utils import timezone

from rideshare.models import Vehicle
from django.contrib.auth.models import User

    reg_no = models.CharField(max_length=8)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    user = models.ForeignKey(User, primary_key=True)

def populate():
	add_vehicle(user='Harry',
	reg_no='SJ01 5PU',
	make='Ford',
	model='Escort')

	
	add_vehicle(user='leifos',
	reg_no='LE1 7OS',
	make='Aston Martin',
	model='DB9')
	
def add_add_vehicle(user, reg_no, make, model):
	a = Review.objects.get_or_create(user=user)[0]
	a.reg_no=reg_no
	a.make=make
	a.model=model
	a.save()
	return a
	
if __name__ == '__main__':
	print "Starting population script"
	populate()