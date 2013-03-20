from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('followup.views',
    # Examples:
    # url(r'^$', 'followup.views.home', name='home'),
    # url(r'^followup/', include('followup.foo.urls')),
    url(r'^add/', 'add'),
    url(r'^add_url', 'add_url'),
    url(r'^respond', 'respond'),
    url(r'^list', 'list_page'),
    url(r'^process_login', 'process_login'),
    url(r'^process_logout', 'process_logout'),
    url(r'^login', TemplateView.as_view(template_name='login.html')), 
    url(r'^$', TemplateView.as_view(template_name='index.html')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
