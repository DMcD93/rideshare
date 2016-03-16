import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rideshare_project.settings")

import django
django.setup()

from rideshare.models import Journey


def populate():
    add_journey(departure = 'Great Western Road',
        destination ='University Avenue',
		travelling_date ="2016-02-01",
		travelling_time ="09:03",
        is_return=True)

    add_journey(departure = 'Partick Station',
        destination ='Briars Road',
		travelling_date ="2016-02-20",
		travelling_time ="08:30",
        is_return=False)
		
    add_journey(departure = 'Glasgow Central Rail Station',
        destination ='Great Western Road',
		travelling_date ="2016-02-07",
		travelling_time ="13:15",
        is_return=False)

    # Print out what we have added to the user.
    #for j in Journey.objects.all:
    #    print "- {0} - {1}".format(str(j))

def add_journey(departure, destination, travelling_date, travelling_time, is_return):
    j = Journey.objects.create()
    j.departure=departure
    j.destination=destination
    j.travelling_date=travelling_date
    j.travelling_time=travelling_time
    j.is_return=is_return
    j.save()
    return j

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()