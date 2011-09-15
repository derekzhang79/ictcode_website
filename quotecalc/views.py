from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import DetailView

from models import Task, Quote
from forms import QuoteForm


def create(request, tasks=Task.objects.all(),
           template='quotecalc/create.html'):
    if request.method == 'POST':
        form = QuoteForm(request.POST)

        if form.is_valid():
            quote = form.save()

            quote.lock_price()
            quote.save()

            return redirect('quotecalc-detail', pk=quote.id)
    else:
        form = QuoteForm(tasks=tasks)

    response_data = {
        'quote_form': form,
        'tasks': tasks,
    }

    return render_to_response(template, response_data,
                              context_instance=RequestContext(request))


class QuoteDetailView(DetailView):
    queryset = Quote.objects.all()
    template_name = 'quotecalc/detail.html'
