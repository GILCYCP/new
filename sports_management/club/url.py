from django.conf.urls import url
from club import views

urlpatterns=[
    url('club registration/',views.locate),
    url('manage/',views.manage),
    url('app/(?P<idd>\w+)',views.apprv,name='ap'),
    url('rej/(?P<idd>\w+)',views.reject,name='re'),
    url('user/',views.userview),
    url('bk/(?P<idd>\w+)',views.book)

]