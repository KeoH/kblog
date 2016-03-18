from django.shortcuts import render
from django.views.generic import ListView

from braces.views import LoginRequiredMixin

from kstore.helpers.mixins import JerarquiaMixin
from kblog.models import Post

class AllPostManagerView(LoginRequiredMixin,JerarquiaMixin,ListView):
    jerarquia = ['Blog', 'All posts']
    model = Post
