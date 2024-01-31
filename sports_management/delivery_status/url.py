from django.conf.urls import url
from delivery_status import views

urlpatterns=[
    url('delivery/',views.delivery),
    url('view/',views.viewdelivery)
]