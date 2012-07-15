from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worksite.views.home', name='home'),
    # url(r'^worksite/', include('worksite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^work_survey/$', 'work_survey.views.index'),
    url(r'^work_survey/(?P<poll_id>\d+)/$', 'work_survey.views.detail'),
    url(r'^work_survey/(?P<poll_id>\d+)/results/$', 'work_survey.views.results'),
    url(r'^work_survey/(?P<poll_id>\d+)/vote/$', 'work_survey.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)
