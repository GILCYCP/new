from django.conf.urls import url
from advertisement import views


urlpatterns=[
    url('post/',views.post),
    url('viewadd/',views.viewads),
    url('mngadv/',views.mngads),
    url('aprv/(?P<idd>\w+)',views.aprl,name='aprl'),
    url('rejct/(?P<idd>\w+)',views.rejt,name='rejt'),
    url('post_shop/',views.post_shop),
    url('adminpst/', views.post_shop_admin)
]