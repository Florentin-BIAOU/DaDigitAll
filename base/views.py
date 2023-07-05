from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.


def home(request):

    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get("message")
        subject = f'Message de site DADIGITALL venant de {name} ({email})'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['hountondjisenek@gmail.com']
        print(name, email, message)
        send_mail(subject,message,from_email,recipient_list)
        messages.success(request, 'Votre message a été envoyé avec succes!')
        #return redirect('home')
    
    context={'scroll_nav': True}
    return render(request, 'home.html', context)
   


def blog(request):
    context = {}
    return render(request, 'blog.html', context)


def apropos(request):
    context={'scroll_nav': False}
    return render(request, 'apropos.html', context)



