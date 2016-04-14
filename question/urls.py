from django.conf.urls import url
from . import views
urlpatterns=[url(r'^list/',views.list_ques,name='list'),
 url(r'^add/',views.ques_add,name='add'),
 url(r'edit/(?P<id>[0-9]+)/',views.ques_edit,name='edit'),
 url(r'myques/',views.myques,name='myques'),
 url(r'answers/(?P<id>[0-9]+)/',views.ans,name='ans')]
