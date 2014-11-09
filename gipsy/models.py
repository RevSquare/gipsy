from django.db import models
from django.utils.translation import ugettext_lazy as _


class GipsyMenu(models.Model):
    """
    Model managing the menu displayed in the toolbar. The menu items reference
    to each other to display a parent and its children
    """
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(_('Name'), max_length=255)
    url = models.CharField(_('Url'), blank=True, null=True, max_length=255)
    order = models.PositiveSmallIntegerField('Order')

    class Meta:
        ordering = ['order']
        abstract = True

    def __unicode__(self):
        return self.name

    @property
    def url_has_domain(self):
        return self.url.startswith('http')

    @property
    def path(self):
        return '/' + self.url
