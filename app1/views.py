from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from app1.models import Profile

#from .forms import SignupForm,EditForm,UserDetail

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 

from django.contrib.auth.models import User



def Home(request):
    return render(request,'home.html')


def rentlist(request):
    users = User.objects.all().select_related('profile')
    return render(request, 'rentlist.html',{'users':users})

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request,'signup.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)   


def changepassword(request):
    pass

def contactus(request):
    return render(request,'contact.html')

'''
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile')
        else:
            form =  AuthenticationForm()
        return render(request,'userlogin.html',{'form':form})
    else:
        return HttpResponseRedirect('/profile') 


@login_required
def userprofile(request):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditForm(request.POST,instance=request.user)
            forms = UserDetail(request.POST,instance=request.user.profile)

            if  form.is_valid() and forms.is_valid(): 
                form.save()
                forms.save() 
                return redirect('/profile')   
        
        else:
            form = EditForm(instance=request.user)
            forms = UserDetail(instance=request.user.profile)

        return render(request,'profile.html',{'form':form,'forms':forms})
    else:
        return HttpResponseRedirect('/login')  

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login')    
'''


