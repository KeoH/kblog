from django.db import models

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

from kblog.models import Category, Publication

class PostManager(models.Manager):
    def for_slider(self):
        return self.filter(
            published = True
        ).order_by('-published_at')[:3]

    def for_index_postlist(self, number):
        return self.filter(
            published = True
        ).order_by('-published_at')[:number]


class Post(Publication):
    """
        Modelo para los posts del blog.
    """
    preview_body = RichTextField(config_name='mail_ckeditor', blank=True)
    category = models.ForeignKey(Category, verbose_name='Categoria')
    heading_image = models.ImageField(blank=True)
    tags = TaggableManager(
        verbose_name='Tags',
        help_text="A comma-separated list of tags",
        blank=True
    )
    objects = PostManager()
    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
