from django.conf import settings


def reformat_settings():
    """Makes sure request object is in the context processor"""
    if not 'django.core.context_processors.request' in settings.TEMPLATE_CONTEXT_PROCESSORS:
        settings.TEMPLATE_CONTEXT_PROCESSORS = \
            settings.TEMPLATE_CONTEXT_PROCESSORS + ('django.core.context_processors.request',)


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
