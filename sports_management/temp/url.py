from django.conf.urls import url
from temp import views


urlpatterns = [
     url('admn/',views.admin),
     url('club/',views.club_manage),
     url('home/',views.home),
     url('shop/',views.shop),
     url('user/',views.user),
 ]