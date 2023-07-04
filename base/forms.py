from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    option = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)