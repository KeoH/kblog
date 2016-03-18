from django.db import models

from ckeditor.fields import RichTextField


class Publication(models.Model):
    """
        Modelo abstracto para una publicacion (Post o Page)
    """
    title = models.CharField('Titulo', max_length=255)
    body = RichTextField(config_name='mail_ckeditor', blank=True)
    body_draft = RichTextField(config_name='mail_ckeditor', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
