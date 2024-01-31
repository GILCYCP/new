from django.conf.urls import url
from games import views

urlpatterns = [
    url('addgame/',views.addgame),
    url('viewgame/',views.viewgame)

]