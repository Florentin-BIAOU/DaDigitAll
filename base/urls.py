from django.urls import path 
from . import views

urlpatterns = [
    #path('',views.home, name="Home"),

    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('apropos/', views.apropos, name='apropos'),

    path('contact/', views.contact_view, name='contact'),
    path('confirmation/', views.confirmation_view, name='confirmation'),
]

