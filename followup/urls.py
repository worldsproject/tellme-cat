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
    url(r'^add_url', 'add'),
    url(r'^add', 'add_page'),
    url(r'^delete', 'delete'),
    url(r'^respond_url', 'respond'),
    url(r'^respond', 'respond_page'),
    url(r'^list', 'list_page', name='list'),
    url(r'^profile', 'view_profile'),
    url(r'^updates', FollowUps()),
    url(r'^$', 'home'),
    url(r'^privacy', TemplateView.as_view(template_name='privacy.html')),
    url(r'^browserid/', include('django_browserid.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
