from django import forms
from django.core.mail.backends.dummy import EmailBackend as DummyEmailBackend
from django.core.mail import BadHeaderError, EmailMessage, get_connection

import settings


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    company = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)
    message = forms.CharField(widget=forms.widgets.Textarea())

    def clean(self):
        try:
            self.send_mail(DummyEmailBackend())
        except BadHeaderError:
            raise forms.ValidationError('Invalid header found.')

        return self.cleaned_data

    def send_mail(self, connection=None):
        name = self.cleaned_data.get('name', None)
        email = self.cleaned_data.get('email')
        company = self.cleaned_data.get('company')
        phone_number = self.cleaned_data.get('phone_number')
        message = self.cleaned_data.get('message')

        if name and company:
            subject = 'Contact: {0} ({1})'.format(name, company)
        else:
            subject = 'Contact: {0}'.format(name)

        body = '{0}\n\n'.format(message)

        body = '{0}{1}\n{2}\n'.format(body, name, email)

        if phone_number:
            body = '{0}\n{1}'.format(body, phone_number)

        connection = connection or get_connection()

        # headers needs to be specified in the constructor for it to work
        e = EmailMessage(headers={'Reply-To': email})
        
        e.subject = subject
        e.body = body 
        e.to = [settings.CONTACT_EMAIL,]
        e.connection = connection
        
        e.send()
