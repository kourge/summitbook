from django.conf.urls.defaults import *

from . import views

urlpatterns = patterns('',
    url('', views.index, name='people.index'),
)
