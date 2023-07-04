from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home, name="Home"),
     path('contact/', views.contact_view, name='contact'),
    path('confirmation/', views.confirmation_view, name='confirmation'),
]

