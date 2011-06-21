from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.mail import send_mail, BadHeaderError

from forms import ContactForm
import settings

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            company = form.cleaned_data['company']
            message = form.cleaned_data['message']
            
            if name and company:
                subject = '{0} ({1})'.format(name, company)
            else:
                subject = name
                
            message = '{0}\n\n{1}'.format(message, name)
            
            if (phone_number):
                message = '{0}\n{1}'.format(message, phone_number)
                
            try:
                send_mail(subject, message, email, zip(*settings.MANAGERS)[1])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                
            return redirect('thanks')
    else:
        form = ContactForm()
        
    response_data = {
        'contact_form': form
    }

    return render_to_response('contact.html', response_data,
                              context_instance=RequestContext(request))
