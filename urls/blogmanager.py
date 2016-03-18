#encoding:utf-8
from django.conf.urls import include, url

from kblog.views.blogmanager import AllPostManagerView

urlpatterns = [
    url(r'^$', AllPostManagerView.as_view(), name='allpost'),
]
