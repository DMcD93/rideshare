from django import forms
from django.contrib.auth.models import User
<<<<<<< HEAD
from rideshare.models import Users_Reg, Journey

class DateInput(forms.DateInput):
    input_type = 'date'
	
class TimeInput(forms.DateInput):
    input_type = 'time'
=======
from rideshare.models import Users_Reg, Vehicle, Journey
>>>>>>> ef1b18c25a227eb7cf2fb0110531c0ce42609319

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserRegForm(forms.ModelForm):
<<<<<<< HEAD
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
=======
	
	class Meta:
		model = Users_Reg
		fields = ('phone', 'age', 'identity_number')

>>>>>>> ef1b18c25a227eb7cf2fb0110531c0ce42609319
