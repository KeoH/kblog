#encoding:utf-8
from django.conf.urls import include, url

from kblog.views.blog import AllPostView, PostView

urlpatterns = [
    url(r'^$', AllPostView.as_view(), name='allpost'),
    url(r'^(?P<pk>[-\w]+)/$', PostView.as_view(), name='post-detail'),
]
