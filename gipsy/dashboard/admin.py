from functools import update_wrapper
from importlib import import_module

from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.conf import settings
from django.conf.urls import patterns, url
from django.template.response import TemplateResponse

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
            url(r'^$', wrap(self.dashboard), name='index'),
            url(r'^all-apps$',
                wrap(self.index),
                name='all_apps')
        )
        return urlpatterns + default_urlpatterns

    def init_dashboard_class(self):
        dashboard_module = getattr(
            settings,
            'GIPSY_DASHBOARD',
            'gipsy.dashboard.presets.default.DashboardDefault'
        )
        mod, inst = dashboard_module.rsplit('.', 1)
        mod = import_module(mod)
        return getattr(mod, inst)

    def dashboard(self, request):
        """
        Displays the dashboard on the main page and triggers widget
        from the settings.GIPSY_DASHBOARD constant.
        """
        request.current_app = self.name
        context = dict(
            dashboard=self.init_dashboard_class()(request),
        )
        return TemplateResponse(request, 'admin/dashboard.html', context)

if not hasattr(settings, 'GIPSY_ENABLE_ADMINSITE') or \
   settings.GIPSY_ENABLE_ADMINSITE is not False:
    admin.site = GipsyAdminSite(name='gipsy_admin')
admin.site.register(GipsyDashboardMenu, GipsyDashboardMenuAdmin)
