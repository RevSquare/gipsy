from django.conf import settings


def reformat_settings():
    """Makes sure request object is in the context processor"""
    if not 'django.core.context_processors.request' in settings.TEMPLATE_CONTEXT_PROCESSORS:
        settings.TEMPLATE_CONTEXT_PROCESSORS = \
            settings.TEMPLATE_CONTEXT_PROCESSORS + ('django.core.context_processors.request',)
