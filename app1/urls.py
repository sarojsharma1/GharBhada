from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('rentlist/',views.rentlist,name="find rent"),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('contact',views.contactus,name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',views.userlogout,name='logout'),
     path('changepass',views.changepassword,name='changepass'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    #path('login/',views.userlogin,name='login'),   
] 
