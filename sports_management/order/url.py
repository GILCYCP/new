from django.conf.urls import url
from order import views

urlpatterns = [
    # url('placeorder/', views.placeorder),
    url('vieworder/', views.vieworder),
    url('mngodr/',views.mngorder),
    url('aprv/(?P<idd>\w+)',views.aprl,name='vv'),
    url('rejct/(?P<idd>\w+)',views.rejt,name='cc'),


]