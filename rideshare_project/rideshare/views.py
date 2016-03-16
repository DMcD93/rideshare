# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rideshare.forms import UserForm, UserRegForm
#from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from rideshare.models import Journey

def main(request):
	return render(request, 'rideshare/main.html')	
#    return HttpResponse("This is the main page")

def login(request):
	return render(request, 'rideshare/login.html')	

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
