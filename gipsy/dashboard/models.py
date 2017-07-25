from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..models import GipsyMenu


class GipsyDashboardMenu(GipsyMenu):
    icon = models.CharField(_('icon'), max_length=20,
                            help_text=_("Font awesome class \
                                        http://fortawesome.github.io/Font-Awesome/icons/\
                                         ie: fa-circle"))
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    _url_args = None
    _original_url = None

    def __init__(self, *args, **kwargs):
        super(GipsyDashboardMenu, self).__init__(*args, **kwargs)
        self._original_url = self.url

    @property
    def children(self):
        return GipsyDashboardMenu.objects.filter(parent=self.pk)

    def get_url_args(self):
        """
        Get the arguments from the url.
        """
        if self._url_args is None:
            if self.url is None:
                self._url_args = []
                return self._url_args
            url = self.url
            if url[0] != '/':
                url = '/' + url
            self._url_args = url.split('/')
        return self._url_args
