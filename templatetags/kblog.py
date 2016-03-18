from django import template

from kstore.helpers.themes import get_theme_url

from kblog.models import Post, Menu

register = template.Library()

@register.inclusion_tag(get_theme_url()+'/parts/slider.html')
def get_slider():
    postlist = Post.objects.for_slider()
    return {'postlist':postlist}

@register.inclusion_tag(get_theme_url()+'/parts/postlist.html')
def get_postlist(number=5):
    postlist = Post.objects.for_index_postlist(number)
    return {'postlist':postlist}

@register.inclusion_tag(get_theme_url()+'/parts/menu.html')
def get_menu(name="MainMenu"):

    menu_nodes = Menu.objects.get(name=name)

    return {"nodes": menu_nodes}
