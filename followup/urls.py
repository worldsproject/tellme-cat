from django.conf.urls import patterns, include, url

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
    url(r'^process_login', 'process_login'),
    url(r'^login', 'login'), 

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
