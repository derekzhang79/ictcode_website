from django import forms
from django.core.mail.backends.dummy import EmailBackend as DummyEmailBackend
from django.core.mail import BadHeaderError, EmailMessage, get_connection

import settings


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField(required=False)
    company = forms.CharField(required=False)
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
        phone_number = self.cleaned_data.get('phone_number')
        company = self.cleaned_data.get('company')
        message = self.cleaned_data.get('message')

        if name and company:
            subject = 'Contact: {0} ({1})'.format(name, company)
        else:
            subject = 'Contact: {0}'.format(name)

        body = '{0}\n\n{1}'.format(message, name)

        if (phone_number):
            body = '{0}\n{1}'.format(body, phone_number)

        connection = connection or get_connection()

        EmailMessage(subject, body, email, zip(*settings.MANAGERS)[1],
                     connection=connection).send()
