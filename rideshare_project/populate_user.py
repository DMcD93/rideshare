import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rideshare_project.settings")

import django
django.setup()

from rideshare.models import Users_Reg
from django.contrib.auth.models import User

def populate():

	user_name_1 = add_user_main(username='Harry',
	password='harry',
	email='harry@abc.com',
	first_name='Harry',
	last_name='Potter')
	
	add_users(user=user_name_1,
	phone = '123456560',
	age ='34',
	identity_number='2196734')
	
	user_name_2 = add_user_main(username='Sally',
				password='sally',
				email='sally@abc.com',
				first_name='Sally',
				last_name='M')
	
	add_users(user=user_name_2,
	phone = 6789054321,
	age = 25,
	 identity_number= 's2154657')


	user_name_3 = add_user_main(username='leifos',
	password='leifos',
	email='leifos@awesome.com',
	first_name='Leif',
	last_name='Azzopardi')

	add_users(user=user_name_3,
	phone = '123456560',
	age ='34',
	identity_number='2196733')


	user_name_4 = add_user_main(username='laura',
	password='laura',
	email='laura@abc.com',
	first_name='Laura',
	last_name='XYZ')

	add_users(user=user_name_4,
	phone = '123456560',
	age ='34',
	identity_number='2196734')

	user_name_5 = add_user_main(username='david',
	password='david',
	email='david@abc.com',
	first_name='David',
	last_name='Smith')

	add_users(user=user_name_5,
	phone = '123456560',
	age ='29',
	identity_number='2196735')


'''
	for b in User.objects.all():
		for a in Users_Reg.objects.filter(username=b):
			print "-{0} - {1}".format(str(a), str(b))
	'''		
			
def add_user_main(username, password, email, first_name, last_name):
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
	
	
def add_users(user, phone, age, identity_number):
	a = Users_Reg.objects.get_or_create(user=user, phone=phone)[0]
	#a.phone=phone
	a.age=age
	a.identity_number=identity_number
	a.save()
	return a

# Start execution here!
if __name__ == '__main__':
	print "Starting population script..."
	

	populate()