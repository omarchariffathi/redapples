from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'g.views.home', name='home'),
    url(r'^g/', include('g.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'my_project.views.login'),
    url(r'^accounts/logout/$', 'my_project.views.logout'),
    url(r'^accounts/auth/$', 'my_project.views.auth_view'),
    url(r'^accounts/logged_in/$', 'my_project.views.logged_in'),
    url(r'^accounts/invalid/$', 'my_project.views.invalid_login'),

    url(r'^accounts/register/$', 'my_project.views.register_user'),
    url(r'^accounts/register_success/$', 'my_project.views.register_success'),
)
