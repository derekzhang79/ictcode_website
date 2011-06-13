from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField(required=False)
    company = forms.CharField(required=False)
    description = forms.CharField(widget=forms.widgets.Textarea())
