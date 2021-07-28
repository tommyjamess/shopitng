from django.urls import path 
from . import views 


urlpatterns = [
    path('signup_form/', views.signupform, name='signupform'),
    path('registerform/', views.registerform, name='register'),
    path('user_profile/', views.userprofile, name='userprofile'),
    path('profile_update/', views.profileupdate, name='profileupdate'),
    path('login/', views.loginform, name='login'),
    path('logout/', views.logoutfunc, name='logout'),
]
