from django.conf import settings
if 'gipsy.dashboard' in settings.INSTALLED_APPS:
    from gipsy.dashboard.admin import admin
else:
    from django.contrib import admin

from ..admin import GipsyMenu, ChildrenInline
from .models import GipsyToolbarMenu


class ChildrenToolbarInline(ChildrenInline):
    model = GipsyToolbarMenu


class GipsyToolbarMenuAdmin(GipsyMenu):
    inlines = [ChildrenToolbarInline]

admin.site.register(GipsyToolbarMenu, GipsyToolbarMenuAdmin)
