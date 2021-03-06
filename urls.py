from django.conf import settings
from django.conf.urls.defaults import *


urlpatterns = patterns('',
    ('^$', include('people.urls')),
    ('^people/', include('people.urls')),
)

if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
