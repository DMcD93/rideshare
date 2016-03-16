from django import forms
from django.contrib.auth.models import User
from rideshare.models import Users_Reg, Vehicle, Journey

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserRegForm(forms.ModelForm):
	
	class Meta:
		model = Users_Reg
		fields = ('phone', 'age', 'identity_number')

