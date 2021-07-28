from django import forms 
from django.forms import ModelForm 
from django.forms import TextInput, EmailInput, FileInput, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


from .models import UserProfile

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='username')
    first_name = forms.CharField(max_length=50, help_text='firstname')
    last_name = forms.CharField(max_length=50, help_text='lastname')
    email = forms.EmailField(max_length=50, help_text='email')


    class Meta:
        model = User
        fields =('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user 


STATE =[
    ('Abia', 'Abia'),
    ('Adamawa', 'Akwa-ibom'),
    ('Edo', 'Edo'),
    ('Imo', 'Imo'),
    ('Lagos', 'Lagos'),
    ('Ondo', 'Ondo'),
    ('Abia', 'Umaya'),
    ('Adamawa', 'Yola'),
    ('Bauchi', 'Bauchi'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone', 'address', 'city', 'state', 'country', 'image')
        widgets = {
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            'last_name':  TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
            'middle_name':  TextInput(attrs={'class': 'input', 'placeholder': 'Middle Name'}),
            'email':  EmailInput(attrs={'class': 'input', 'placeholder': 'Email Adress'}),
            'phone':  TextInput(attrs={'class': 'input', 'placeholder': 'Phone'}),
            'address':  TextInput(attrs={'class': 'input', 'placeholder': 'Address'}),
            'city':  TextInput(attrs={'class': 'input', 'placeholder': 'city'}),
            'state':  Select(attrs={'class': 'input', 'placeholder': 'State'}, choices=STATE),
            'country':  TextInput(attrs={'class': 'input', 'placeholder': 'country'}), 
            'image':  FileInput(attrs={ 'placeholder': 'image'}),
        }