# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from rideshare.forms import UserForm, UserRegForm
#from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rideshare.models import Journey

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
                return HttpResponseRedirect('/rideshare/')
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
    return HttpResponseRedirect('/rideshare/')

def register(request):
	registered = False

	if request.method == 'POST':

        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		profile_reg = UserRegForm(data=request.POST)
        
       
		if user_form.is_valid() and profile_reg.is_valid():
           
			user = user_form.save()

            		user.set_password(user.password)
			user.save()

			profile = profile_reg.save(commit=False)
			profile.user = user
			profile.save()
        

            		registered = True
			#success_message = "Registration Successful"
			#messages.success(request, 'Profile details updated.')

		else:
			print user_form.errors, profile_reg.errors
			#messages.error(request, 'Document deleted.')

   	else:
		user_form = UserForm()
		profile_reg = UserRegForm()
       
    # Render the template depending on the context.
	return render(request, 'rideshare/registration.html', 
			{'user_form': user_form, 'profile_reg': profile_reg, 'registered': registered} )

	#return render(request, 'rideshare/register.html')	

def post_ride(request):
	return render(request, 'rideshare/login.html')	
	
def search_ride(request):
    journey_list = Journey.objects.order_by('-travelling_date', 'travelling_time')
    context_dict = {'journeys': journey_list}

    return render(request, 'rideshare/searchRide.html', context_dict)	
	
def search_ride_departure(request):
    journey_list = Journey.objects.order_by()
    context_dict = {'journeys': journey_list}

    return render(request, 'rideshare/searchRide.html', context_dict)
