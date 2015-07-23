# coding: utf-8

# DJANGO IMPORTS
from django.conf import settings

# Enable GIPSY admin site
GIPSY_ENABLE_ADMINSITE = getattr(settings, "GIPSY_ENABLE_ADMINSITE", True)


GIPSY_DASHBOARD_URL = getattr(settings, "GIPSY_DASHBOARD_URL", 'admin:index')
GIPSY_DASHBOARD_TITLE = getattr(settings, "GIPSY_DASHBOARD_TITLE", 'ADMINISTRATION')
GIPSY_DASHBOARD_HAS_ROWS = getattr(settings, "GIPSY_DASHBOARD_HAS_ROWS", True)
GIPSY_DASHBOARD_DEFAULT_GRID = getattr(settings, "GIPSY_DASHBOARD_DEFAULT_GRID", 12)
GIPSY_DASHBOARD_CACHE_TIME = int(getattr(settings, "GIPSY_DASHBOARD_CACHE_TIME", 500))
GIPSY_VANILLA_INDEX_URL = \
    getattr(settings, "GIPSY_VANILLA_INDEX_URL", 'admin:all_apps')
GIPSY_THEME = getattr(settings, "GIPSY_THEME",
                      getattr(settings, "STATIC_URL", "")
                      + 'gipsy_dashboard/css/gipsy.css')
