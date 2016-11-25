from django.contrib import admin

from ..admin import GipsyMenu, ChildrenInline
from .models import GipsyDashboardMenu


class ChildrenDashboardInline(ChildrenInline):
    model = GipsyDashboardMenu
    exclude = ('icon',)


class GipsyDashboardMenuAdmin(GipsyMenu):
    inlines = [ChildrenDashboardInline]
    exclude = ('url', 'parent',)

admin.site.register(GipsyDashboardMenu, GipsyDashboardMenuAdmin)
