from django.conf.urls import url
from . import views
urlpatterns=[
url(r'add/(?P<id>[0-9]+)/',views.add,name='postans'),
url(r'edit/(?P<id>[0-9]+)/',views.edit,name='edit answer')]