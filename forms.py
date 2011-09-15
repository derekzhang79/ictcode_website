from django import forms
from django.core.mail.backends.dummy import EmailBackend as DummyEmailBackend
from django.core.mail import BadHeaderError, EmailMessage, get_connection

from quotecalc.models import Quote

import settings


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    company = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)
    quote_number = forms.IntegerField(required=False)
    message = forms.CharField(widget=forms.widgets.Textarea())

    def clean(self):
        try:
            self.send_mail(DummyEmailBackend())
        except BadHeaderError:
            raise forms.ValidationError('Invalid header found.')

        quote_number_id = self.cleaned_data.get('quote_number')

        try:
            Quote.objects.get(id=quote_number_id)
        except Quote.DoesNotExist:
            raise forms.ValidationError('Invalid quote number.')

        return self.cleaned_data

    def send_mail(self, connection=None):
        name = self.cleaned_data.get('name', None)
        email = self.cleaned_data.get('email')
        company = self.cleaned_data.get('company')
        phone_number = self.cleaned_data.get('phone_number')
        quote_number = self.cleaned_data.get('quote_number')
        message = self.cleaned_data.get('message')

        if name and company:
            subject = 'Contact: {0} ({1})'.format(name, company)
        else:
            subject = 'Contact: {0}'.format(name)

        body = '{0}\n\n'.format(message)

        if quote_number:
            body = 'Quote #{0}{1}\n'.format(body, quote_number)

        body = '{0}{1}\n'.format(body, name)

        if phone_number:
            body = '{0}\n{1}'.format(body, phone_number)

        connection = connection or get_connection()

        EmailMessage(subject, body, email, zip(*settings.MANAGERS)[1],
                     connection=connection).send()
