from django.contrib import admin

from kblog.models import Post, Category, Menu, MenuItem, Link, Page

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'published']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Link)
admin.site.register(Page)
