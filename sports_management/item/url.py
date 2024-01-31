from django.conf.urls import url
from item import views

urlpatterns = [
    url('item/',views.item),
    url('viewitems/',views.viewitem),
    url('order/(?P<idd>\w+)',views.order,name='pp'),

]