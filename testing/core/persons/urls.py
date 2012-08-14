from django.conf.urls.defaults import patterns, include, url


urlpatterens = patterns('core.persons.views',

    url(r'^persons/$' ,'staff_members'),
    url(r'^persons/(?P<staff_id>)/$','staff'),
    url(r'^persons/details/$', 'resident_profile')

)
