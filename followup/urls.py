from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('followup.views',
    # Examples:
    # url(r'^$', 'followup.views.home', name='home'),
    # url(r'^followup/', include('followup.foo.urls')),
    url(r'^add_url', 'add'),
    url(r'^add', login_required(TemplateView.as_view(template_name='add_url.html'))),
    url(r'^delete', 'delete'),
    url(r'^respond_url', 'respond'),
    url(r'^respond', login_required(TemplateView.as_view(template_name='respond.html'))),
    url(r'^register_user', 'register_user'),
    url(r'^register', TemplateView.as_view(template_name='register.html')),
    url(r'^list', 'list_page'),
    url(r'^process_login', 'process_login'),
    url(r'^process_logout', 'process_logout'),
    url(r'^login', TemplateView.as_view(template_name='login.html')), 
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^browserid/', include('django_browserid.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
