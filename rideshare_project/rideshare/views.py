# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from rideshare.forms import UserForm, UserRegForm, JourneyForm, VehicleForm, ReviewForm, SearchForm
#from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rideshare.models import Journey, Vehicle, Passanger, User, Review, Users_Reg
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
from django.db.models import Q

def main(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			search_form = SearchForm(data=request.POST)
			if search_form.is_valid():
				departure = request.POST.get('departure')
				departure = departure.split(',')
				
				destination = request.POST.get('destination')
				destination = destination.split(',')			

				journey_list = Journey.objects.filter(departure=departure[0], destination=destination[0])
				passanger_list = Passanger.objects.all()
				context_dict = {'journeys': journey_list, 'passangers': passanger_list}

				return render(request, 'rideshare/searchRide.html', context_dict)	
			else:
				print search_form.errors
		else:
			search_form = SearchForm()
	else:
		return render(request, 'rideshare/main.html')

	return render(request, 'rideshare/main.html', {'search_form': search_form})
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
        #request.session['username_session']=user.username
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
            {'user_form': user_form, 'reg_form': reg_form, 'registered': registered})

def post_ride(request):
	successful = False

	if request.user.is_authenticated():		
		# If it's a HTTP POST, we're interested in processing form data.
		if request.method == 'POST':
			# Attempt to grab information from the raw form information.
			# Note that we make use of both UserForm and UserProfileForm.
			journey_form = JourneyForm(data=request.POST)
			
			try:
				vehicle = Vehicle.objects.get(user__username=request.user)
			except Exception as e:
				 return HttpResponseRedirect('/add_vehicle')
		
			# If the two forms are valid...
			if journey_form.is_valid():
				# Save the user's form data to the database.
				journey = journey_form.save(commit=False)
				journey.user = vehicle
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
		journey_list = Journey.objects.filter(Q(travelling_date=datetime.datetime.now().strftime('%Y-%m-%d'),travelling_time__gte=datetime.datetime.now().strftime('%H:%M'))|Q(travelling_date__gt=datetime.datetime.now().strftime('%Y-%m-%d'))).order_by('travelling_date', 'travelling_time', 'cost')
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

@login_required	 
def get_user_profile(request):
	profile_info = Users_Reg.objects.get(user__username = request.user)
	
	exists = False
	
	try:
		vehicle_list = Vehicle.objects.get(user__username = request.user)
		if not vehicle_list is None:
			review_list = Review.objects.filter(user__username = request.user).order_by('-posted_at')[:3]
			exists = True
			return render(request, 'rideshare/profile.html', {'profile': request.user, 'profile_info': profile_info, 'vehicle': vehicle_list,
					'review_list':review_list, 'exists': exists})
	except:
		return render(request, 'rideshare/profile.html', {'profile': request.user, 'profile_info': profile_info, 'exists': exists})


@login_required				
def ridesposted(request):
	ride_list = Journey.objects.filter(user = request.user)
				
	context_dict = {'rides': ride_list}

	return render(request, 'rideshare/ridesPosted.html', context_dict)	
	
@login_required				
def ridesBooked(request):
	booked_list = Passanger.objects.filter(Q(front = request.user)|Q(backLeft = request.user)|Q(backRight = request.user))	
	ride_list = Journey.objects.all()	
	
	context_dict = {'booked': booked_list, 'rides': ride_list}

	return render(request, 'rideshare/ridesBooked.html', context_dict)	
	
@login_required
def get_ride_detail(request, journey):
	posted = False
	"""
	journey_detail = Journey.objects.filter(journey_id)
	driver_detail = Users_Reg.objects.filter(journey_detail.user)
	
	vehicle_detail = Vehicle.objects.filter(user__username=user)"""
	
	journey_info = Journey.objects.get(pk=journey)
	user_info = User.objects.get(username=journey_info.user)
	driver_info = Users_Reg.objects.get(user__username=journey_info.user)
	vehicle_info = Vehicle.objects.get(user__username=journey_info.user)
	review_list = Review.objects.filter(user__username = journey_info.user).order_by('-posted_at')[:3]
	
	if request.user.is_authenticated():
		if request.method == 'POST':	
			review_form = ReviewForm(data=request.POST)
			if review_form.is_valid():
				review = review_form.save(commit = False)
				review.user = driver_info.user
				review.posted_by = request.user.username
				review.posted_for = journey_info.user
				review.posted_at = datetime.datetime.now().replace(microsecond=0)
				review.save()
				posted = True
			else:
				review_form.errors
		else:
			review_form = ReviewForm(auto_id=False)
	else:
		return render(request, 'rideshare/login.html')
		
	context_dict = {'review_form': review_form, 'journey': journey_info, 'user': user_info, 'driver': driver_info, 'vehicle': vehicle_info, 'review_list': review_list}
    
	return render(request, 'rideshare/rideDetail.html', context_dict)
	'''{'driver_detail':driver_detail, 'journey_detail':journey_detail, 
				'vehicle_detail':vehicle_detail, 'review_form':review_form, 'posted':posted})'''