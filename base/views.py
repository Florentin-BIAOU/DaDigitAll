from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.views.decorators.csrf import requires_csrf_token


@requires_csrf_token
# Create your views here.
def home(request):
    return render(request, 'home-digital-agency-onePage.html')




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            option = form.cleaned_data['option']
            message = form.cleaned_data['message']

            # Créer le corps de l'email
            subject = 'Nouvelle demande de conseil'
            body = f"Nom et Prénoms: {name}\n"
            body += f"Adresse Email: {email}\n"
            body += f"Objet de la demande: {option}\n"
            body += f"Message:\n{message}"

            # Envoyer l'email
            send_mail(subject, body, 'from@example.com', ['mdekadjevi@dadigitall.com'])

            return redirect('confirmation')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def confirmation_view(request):
    return render(request, 'confirmation.html')