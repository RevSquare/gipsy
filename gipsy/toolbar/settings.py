from django.conf import settings


LINK_ENABLED = getattr(settings, 'GIPSY_TOOLBAR_LINK_ENABLED', True)
LINK_CONTEXT_NAME = getattr(
    settings, 'GIPSY_TOOLBAR_LINK_CONTEXT_NAME', 'object')
# GIPSY_TOOLBAR_LINK_INCLUDED_MODELS
# define which models links to admin edit page. If `None` all of the models
# Example:
# GIPSY_TOOLBAR_LINK_INCLUDED_MODELS = ('auth.User',)

LINK_INCLUDED_MODELS = getattr(settings, 'GIPSY_TOOLBAR_LINK_INCLUDED_MODELS',
                               None)

VERSION_INDICATOR = getattr(settings, 'GIPSY_VERSION_INDICATOR', None)
# options are nav, user
VERSION_INDICATOR_LOCATION = getattr(settings,
                                     'GIPSY_VERSION_INDICATOR_LOCATION', 'nav')
