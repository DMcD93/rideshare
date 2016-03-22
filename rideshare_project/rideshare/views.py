# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from rideshare.forms import UserForm, UserRegForm, JourneyForm, VehicleForm
#from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rideshare.models import Journey, Vehicle, Passanger
from django.core.urlresolvers import reverse
from django.views import generic

def main(request):
	return render(request, 'rideshare/main.html')	
#    return HttpResponse("This is the main page")

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your rideshare account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'rideshare/login.html', {})
		
# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        reg_form = UserRegForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and reg_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            reg = reg_form.save(commit=False)
            reg.user = user

            # Now we save the UserProfile model instance.
            reg.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, reg_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        reg_form = UserRegForm()

    # Render the template depending on the context.
    return render(request,
            'rideshare/registration.html',
            {'user_form': user_form, 'reg_form': reg_form, 'registered': registered} )

def post_ride(request):
	successful = False

	if request.user.is_authenticated():		
		# If it's a HTTP POST, we're interested in processing form data.
		if request.method == 'POST':
			# Attempt to grab information from the raw form information.
			# Note that we make use of both UserForm and UserProfileForm.
			journey_form = JourneyForm(data=request.POST)

			vehicle = Vehicle.objects.get(user=request.user)
			
			# If the two forms are valid...
			if journey_form.is_valid():
				# Save the user's form data to the database.
				journey = journey_form.save(commit=False)
				journey.save()
				
				p = Passanger.objects.create(journey=journey)
				p.save()
				successful = True

			# Invalid form or forms - mistakes or something else?
			# Print problems to the terminal.
			# They'll also be shown to the user.
			else:
				print journey_form.errors

		# Not a HTTP POST, so we render our form using two ModelForm instances.
		# These forms will be blank, ready for user input.
		else:
			journey_form = JourneyForm()
			
		# Render the template depending on the context.	
		return render(request,
				'rideshare/postRide.html',
				{'journey_form': journey_form, 'successful': successful} )
				
	else:
		 return HttpResponseRedirect('/login')
	
def search_ride(request):
	if request.user.is_authenticated():
		journey_list = Journey.objects.order_by('travelling_date', 'travelling_time', 'cost')
		passanger_list = Passanger.objects.all()
		context_dict = {'journeys': journey_list, 'passangers': passanger_list}

		return render(request, 'rideshare/searchRide.html', context_dict)	
	else:
		 return HttpResponseRedirect('/login')
		 
def add_vehicle(request):
	successful = False

	if request.user.is_authenticated():		
		# If it's a HTTP POST, we're interested in processing form data.
		if request.method == 'POST':
			# Attempt to grab information from the raw form information.
			# Note that we make use of both UserForm and UserProfileForm.
			vehicle_form = VehicleForm(data=request.POST)

			# If the two forms are valid...
			if vehicle_form.is_valid():
				# Save the user's form data to the database.
				vehicle = vehicle_form.save(commit=False)
				vehicle.user = request.user
				vehicle.save()
				successful = True

			# Invalid form or forms - mistakes or something else?
			# Print problems to the terminal.3
			# They'll also be shown to the user.
			else:
				print vehicle_form.errors

		# Not a HTTP POST, so we render our form using two ModelForm instances.
		# These forms will be blank, ready for user input.
		else:
			vehicle_form = VehicleForm()
			
		# Render the template depending on the context.	
		return render(request,
				'rideshare/addVehicle.html',
				{'vehicle_form': vehicle_form, 'successful': successful} )
				
	else:
		 return HttpResponseRedirect('/login')
		 
def bookSeat(request, journey):
	p = Passanger.objects.get(journey=journey)
	q = Journey.objects.get(pk=journey)
	if p.front is None:
		p.front=request.user
		p.save()
		q.seatsAvailable -= 1
		q.save()
	elif p.backLeft is None:
		p.backLeft=request.user
		p.save()
		q.seatsAvailable -= 1
		q.save()
	else:
		p.backRight=request.user
		p.save()
		q.seatsAvailable -= 1
		q.save()
	return HttpResponseRedirect(reverse('search:search_ride'))
# Create your views here.