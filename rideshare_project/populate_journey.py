import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rideshare_project.settings")

import django
django.setup()

from rideshare.models import Journey, Vehicle, Passanger

def populate():
    add_journey(departure = 'Great Western Road',
        destination ='University Avenue',
		travelling_date ="2016-06-01",
		travelling_time ="09:03",
        seatsAvailable=2,
		cost = 10,
		user="Harry")

    add_journey(departure = 'Partick Station',
        destination ='Byres Road',
		travelling_date ="2016-06-20",
		travelling_time ="08:30",
        seatsAvailable=1,
		cost = 20,
		user="leifos")
		
    add_journey(departure = 'Glasgow Central Rail Station',
        destination ='Great Western Road',
		travelling_date ="2016-06-07",
		travelling_time ="13:15",
        seatsAvailable=1,
		cost = 3,
		user="Harry")

    # Print out what we have added to the user.
    #for j in Journey.objects.all:
    #    print "- {0} - {1}".format(str(j))

def add_journey(departure, destination, travelling_date, travelling_time, seatsAvailable, cost, user):
	v = Vehicle.objects.get(user__username=user)
	j = Journey.objects.get_or_create(departure=departure, destination=destination, travelling_date=travelling_date, 
	travelling_time=travelling_time, seatsAvailable=seatsAvailable, cost=cost, user=v)[0]
	p = Passanger.objects.create(journey=j)
	return j

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()