from django.conf.urls import url
from payment import views

urlpatterns = [
    url('payment/(?P<idd>\w+)',views.payment),
    url('viewpayments/',views.viewpayment),
    url('aprv/(?P<idd>\w+)', views.paprl, name='pa'),
    url('rejct/(?P<idd>\w+)', views.prejt, name='pr'),
    url('shopview/',views.shopviewpayment),
    url('itempay/(?P<idd>\w+)', views.item),
    url('itemaprv/(?P<idd>\w+)', views.s1, name='jj'),
    url('itemrejct/(?P<idd>\w+)', views.s2, name='mm'),
]