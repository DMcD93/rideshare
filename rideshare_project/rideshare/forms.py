from django import forms
from django.contrib.auth.models import User
from rideshare.models import Users_Reg, Journey, Vehicle

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
		fields = ('departure', 'destination', 'travelling_date', 'travelling_time', 'is_return')
		widgets = {
            'travelling_date': DateInput(),
			'travelling_time': TimeInput()
        }
		
class VehicleForm(forms.ModelForm):
	class Meta:
		model = Vehicle
		fields = ('reg_no', 'make', 'model', 'no_of_seats')