from django.conf.urls import url
from shop import views

urlpatterns = [
    url('shopregistration/', views.shop),
    url('shopview/',views.shop_view),
    url('mng/',views.mngshop),
    url('app/(?P<idd>\w+)',views.apprv,name='apr'),
    url('rej/(?P<idd>\w+)',views.rejt,name='rej'),


]