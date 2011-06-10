from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'home.html'}, name='home'),
    url(r'^contact/$', direct_to_template, {'template': 'contact.html'}, name='contact'),
    
    url(r'^404/$', direct_to_template, {'template': '404.html'}, name='404'),
    url(r'^500/$', direct_to_template, {'template': '500.html'}, name='500'),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
