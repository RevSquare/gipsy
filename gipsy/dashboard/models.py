from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..models import GipsyMenu


class GipsyDashboardMenu(GipsyMenu):
    icon = models.CharField(_('icon'), max_length=20,
                            help_text=_("Font awesome class \
                                        http://fortawesome.github.io/Font-Awesome/icons/\
                                         ie: fa-circle"))

    @property
    def children(self):
        return GipsyDashboardMenu.objects.filter(parent=self.pk)
