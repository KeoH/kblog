#encoding:utf-8
from django.views.generic import DetailView, ListView

from kstore.helpers.themes import get_theme_url

from kblog.models import Post, Page

class AllPostView(ListView):
    template_name = get_theme_url() +'/parts/post_list.html'
    model = Post

class PostView(DetailView):
    template_name = get_theme_url() + '/parts/post_detail.html'
    model = Post
    context_object_name = 'post'
