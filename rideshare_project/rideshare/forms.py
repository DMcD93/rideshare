from django import forms
from django.contrib.auth.models import User
from rideshare.models import Users_Reg, Journey, Vehicle, Passanger, Review

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
		
class VehicleForm(forms.ModelForm):
	class Meta:
		model = Vehicle
		fields = ('reg_no', 'make', 'model')
		
class SeatForm(forms.ModelForm):
	class Meta:
		model = Passanger
		fields = ('front',)
		
class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ('description',)
		widgets = {
					'description': forms.Textarea(attrs={'cols':35, 'rows':3})
					}

