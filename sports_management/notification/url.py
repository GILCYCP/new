from django.conf.urls import url
from notification import views

urlpatterns = [
    url('postnotification/', views.postnotification),
    url('viewnotification/', views.viewnotificatin),
    url('post_not_shop/', views.postnotification_shop)

]