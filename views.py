from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.send_mail()

            return redirect('thanks')
    else:
        form = ContactForm()

    response_data = {
        'contact_form': form,
    }

    return render_to_response('contact.html', response_data,
                              context_instance=RequestContext(request))
