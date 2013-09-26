from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from feeds import FollowUps

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('followup.views',
    # Examples:
    # url(r'^$', 'followup.views.home', name='home'),
    # url(r'^followup/', include('followup.foo.urls')),
    url(r'^add_url', TemplateView.as_view(template_name='add_url.html')),
    url(r'^add', 'add'),
    url(r'^delete', 'delete'),
    url(r'^respond_url', 'respond'),
    url(r'^respond', TemplateView.as_view(template_name='respond.html')),
    url(r'^list', 'list_page', name='list'),
    url(r'^profile', TemplateView.as_view(template_name='profile.html')),
    url(r'^updates', FollowUps()),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^privacy', TemplateView.as_view(template_name='privacy.html')),
    url(r'^browserid/', include('django_browserid.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
