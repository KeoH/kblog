from django.db import models

from kblog.models import Post

class Menu(models.Model):
    """
        Clase para el menu que contiene muchos itemsmenu
    """
    name = models.CharField('nombre del menu', max_length=20, blank=False, default='Menu')
    items = models.ManyToManyField('MenuItem')

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    """
        Clase de los items de un menu
    """
    name = models.CharField('nombre del item', max_length=20, blank=False, default='Item')
    position = models.PositiveIntegerField(default=1)
    link = models.ForeignKey('Link', blank=True, null=True)
    submenu = models.ForeignKey(Menu, blank=True, null=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return self.name

class Link(models.Model):
    target = models.ForeignKey(Post)

    def get_id(self):
        return self.target.pk

    def __str__(self):
        return 'Enlace a ' + self.target.title
