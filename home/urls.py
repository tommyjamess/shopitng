from django.urls import path 
from . import views 



urlpatterns = [
    path('', views.index, name='index'),
    path('updateme', views.updateme, name='updateme'),
    path('average/<str:id>', views.average, name='average'),
]
