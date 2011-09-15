from django.conf.urls.defaults import patterns, url, include
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'home.html'}, name='home'),

    url(r'^contact/$', 'views.contact', name='contact'),
    url(r'^contact/(?P<quote_id>\d+)/$', 'views.contact', name='contact'),

    url(r'^quote/', include('quotecalc.urls')),

    url(r'^thanks/$', direct_to_template, {'template': 'thanks.html'},
     name='thanks'),

    url(r'^404/$', direct_to_template, {'template': '404.html'}, name='404'),
    url(r'^500/$', direct_to_template, {'template': '500.html'}, name='500'),

    url(r'^robots\.txt$', direct_to_template,
     {'template': 'robots.txt', 'mimetype': 'text/plain'}, name='robots'),

    url(r'^admin/', include(admin.site.urls), name='admin'),
)
