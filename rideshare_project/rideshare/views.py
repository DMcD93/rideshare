# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from rideshare.forms import UserForm, UserRegForm
#from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login

def main(request):
		return render(request, 'rideshare/main.html')


	#return render(request, 'rideshare/main.html')	
#    return HttpResponse("This is the main page")

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('rideshare/login.html')
				#return render(request, 'rideshare/profile.html')	
			else:
				return HttpResponse("Invalid Login")
				
		else:
			return HttpResponse("Invalid Login1")
	else:
		return render(request, 'rideshare/login.html', {})


	#return render(request, 'rideshare/login.html')	

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
			messages.add_message(request, messages.SUCCESS, 'Registered successfully.')
			
		else:
			print user_form.errors, profile_reg.errors
			messages.add_message(request, messages.ERROR, 'We could not process your request at this time.')

   	else:
		user_form = UserForm()
		profile_reg = UserRegForm()
       
    # Render the template depending on the context.
	return render(request, 'rideshare/registration.html', 
			{'user_form': user_form, 'profile_reg': profile_reg, 'registered': registered} )

	
def post_ride(request):
	return render(request, 'rideshare/login.html')	
	
def profile(request):
	return render(request, 'rideshare/profile.html')

def results(request):
	return render(request, 'rideshare/results.html')