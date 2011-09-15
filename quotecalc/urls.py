from django.conf.urls.defaults import *
from django.contrib import admin

from models import Task
from views import QuoteDetailView

admin.autodiscover()

urlpatterns = patterns('quotecalc',
    url(r'web/$', 'views.create',
     {'tasks': Task.objects.filter(category__name='Web'),
      'template': 'web.html'},
     name='web'),

    url(r'mobile/$', 'views.create',
     {'tasks': Task.objects.filter(category__name='Mobile'),
      'template': 'mobile.html'},
     name='mobile'),

    url(r'desktop/$', 'views.create',
     {'tasks': Task.objects.filter(category__name='Desktop'),
      'template': 'desktop.html'},
     name='desktop'),

    url(r'^(?P<pk>\d+)/$', QuoteDetailView.as_view(), name='quotecalc-detail'),
)
