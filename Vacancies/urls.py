from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^list/$', views.post_list, name='post_list'),
    url(r'^list/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]