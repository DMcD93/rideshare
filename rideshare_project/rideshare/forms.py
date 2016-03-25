from django import forms
from django.contrib.auth.models import User
from rideshare.models import Users_Reg, Journey, Vehicle, Passanger, Review
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'
	
class TimeInput(forms.DateInput):
    input_type = 'time'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserRegForm(forms.ModelForm):
    class Meta:
        model = Users_Reg
        fields = ('phone', 'age', 'identity_number')
		
class JourneyForm(forms.ModelForm):
	class Meta:
		model = Journey
		fields = ('departure', 'destination', 'travelling_date', 'travelling_time', 'cost', 'seatsAvailable')
		widgets = {
            'travelling_date': DateInput(),
			'travelling_time': TimeInput()
        }
		
	def clean_departure(self):
	    departure = self.cleaned_data['departure']
	    departure = departure.split(',')
	    return departure[0]
		
	def clean_destination(self):
	    destination = self.cleaned_data['destination']
	    destination = destination.split(',')
	    return destination[0]
		
	def clean_travelling_date(self):
	    date = self.cleaned_data['travelling_date']
	    if date < datetime.date.today():
		    raise forms.ValidationError("The date cannot be in the past!")
	    return date
		
	def clean_travelling_time(self):
	    time = self.cleaned_data['travelling_time']
	    #convertedTime = datetime.datetime.strptime(time, "%H:%M:%S")
	    #current = datetime.datetime.now().strftime("%H:%M:%S") - dateTime w/o / str w
	    current = datetime.datetime.now().strftime("%H:%M:%S")
		
	    if str(time) < current:
		    raise forms.ValidationError("The time cannot be in the past!")
	    return time
		
class VehicleForm(forms.ModelForm):
	class Meta:
		model = Vehicle
		fields = ('reg_no', 'make', 'model')
		
class SearchForm(forms.ModelForm):
	class Meta:
		model = Journey
		fields = ('departure', 'destination')
		
class ReviewForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea(),label='')
	class Meta:
		model = Review
		fields = ('description',)
		