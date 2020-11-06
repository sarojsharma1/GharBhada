from django import forms
from app1.models import Profile
#from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email']   
        labels = {'email':'Email'} 


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Contactno','image','HallNum','BedNum','kitchenNum','Location','RentCost']
        labels = {'Contactno':'Contact no.','HallNum':'Hall Number','RentCost':'Rent Cost','BedNum':'Bed Number','kitchenNum':'Kitchen Number'} 
'''
    def clean(self):
        cleaned_data = super().clean()    
        valcontact = self.cleaned_data['Contactno']
        valbedno = self.cleaned_data['']
        if len(valcontact) != 10:
            raise forms.ValidationError('Contact Number must be equal to 10')
        if len(valbedno) > 2:
            raise forms.ValidationError('Bed Number must be equal to 100')
'''