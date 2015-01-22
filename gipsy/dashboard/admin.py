from functools import update_wrapper

from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from ..admin import GipsyMenu, ChildrenInline
from .models import GipsyDashboardMenu


class ChildrenDashboardInline(ChildrenInline):
    model = GipsyDashboardMenu
    exclude = ('icon',)


class GipsyDashboardMenuAdmin(GipsyMenu):
    inlines = [ChildrenDashboardInline]
    exclude = ('url', 'parent',)


class GipsyAdminSite(AdminSite):
    def get_urls(self):
        default_urlpatterns = super(GipsyAdminSite, self).get_urls()

        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        urlpatterns = patterns(
            '',
            url(r'^$', wrap(TemplateView.as_view(
                template_name="admin/dashboard.html")), name='index'),
            url(r'^all-apps$',
                wrap(self.index),
                name='all_apps')
        )
        return urlpatterns + default_urlpatterns

if not hasattr(settings, 'GIPSY_ENABLE_ADMINSITE') or \
   settings.GIPSY_ENABLE_ADMINSITE is not False:
    admin.site = GipsyAdminSite(name='gipsy_admin')
admin.site.register(GipsyDashboardMenu, GipsyDashboardMenuAdmin)
