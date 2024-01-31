from django.conf.urls import url
from booking import views

urlpatterns=[
    url('onlinebok/',views.online),
    # url('clubbkng/',views.clubbkg),
    url('view/',views.viewbooking),
    url('mngbkg/',views.mngbooking),
    url('aprv/(?P<idd>\w+)',views.aprl,name='bkg'),
    url('rejct/(?P<idd>\w+)',views.rejt,name='rt'),
    # url('bo/(?P<idd>\w+)',views.book,name='c'),
    # url('clubregistering/',views.clubregi),

]