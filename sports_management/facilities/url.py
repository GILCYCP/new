from django.conf.urls import url
from facilities import views


urlpatterns=[
    url('postfacilities/',views.facilities),
    url('viewfacilities/',views.viewfacilities)

]