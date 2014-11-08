from django import template
from django.conf import settings
from django.core.urlresolvers import resolve

from gipsy.toolbar.models import GipsyToolbarMenu


register = template.Library()


def is_admin(context):
    """Checks if the current request belongs to admin namespace"""
    request = context["request"]
    url = resolve(request.path)
    context['is_admin'] = False
    return url.app_name == 'admin'


@register.inclusion_tag('tags/gipsy_toolbar.html', takes_context=True)
def gipsy_toolbar(context, *args, **kwargs):
    """
    This tags manages the display of the toolbar.
    """
    context['items'] = GipsyToolbarMenu.objects.filter(parent__isnull=True).order_by('order')
    context['logo'] = kwargs.get('logo', '')

    if not context['logo']:
        if hasattr(settings, 'GIPSY_TOOLBAR_LOGO') and settings.GIPSY_TOOLBAR_LOGO:
            context['logo'] = settings.GIPSY_TOOLBAR_LOGO

    context['is_admin'] = is_admin(context)
    return context
