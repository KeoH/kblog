from django.db import models

class Category(models.Model):
    """
        Modelo de las categorias. Para poder organizar los post,
        distinto de los tags.
    """

    ICONS = (
        ('picture-o', 'Picture'),
        ('file-text-o', 'Document'),
        ('video-camera', 'Video'),
        ('music', 'Music'),
    )

    name = models.CharField('Nombre', max_length=128)
    short_description = models.TextField('Descripcion corta', blank=True)
    category_icon = models.CharField('Icono de categoria', max_length=20, choices=ICONS, default='file-text-o')
    def __str__(self):
        return self.name

    def num_post(self):
        return Post.objects.filter(category=self.pk).count()

    class Meta:
        verbose_name_plural = 'Categories'
