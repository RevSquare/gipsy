from django import template
from django.conf import settings
from django.core.urlresolvers import resolve, reverse, NoReverseMatch

from gipsy.toolbar.models import GipsyToolbarMenu
from gipsy.toolbar.settings import LINK_CONTEXT_NAME, LINK_INCLUDED_MODELS, \
    VERSION_INDICATOR, VERSION_INDICATOR_LOCATION


register = template.Library()


def is_admin(context):
    """Checks if the current request belongs to admin namespace"""
    request = context["request"]

    try:
        url = resolve(request.path)
    except:
        # We don't really care to track the type of exception, for
        # whatever it is, it should throw a 500 on the page
        # we should just not display the toolbar in this case
        return False

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


@register.assignment_tag(takes_context=True)
def gipsy_toolbar_link(context):
    """
    :param context: django template context
    :return: link to admin edit page for founded object
    """
    obj = context.get(LINK_CONTEXT_NAME, None)
    if obj is None:
        return None

    app_label = obj.__class__._meta.app_label
    model_name = obj.__class__._meta.object_name
    app_ident = u'%s.%s' % (app_label, model_name)

    if LINK_INCLUDED_MODELS is None or app_ident in LINK_INCLUDED_MODELS:
        try:
            link = reverse('admin:%s_%s_change' % (
                app_label.lower(), model_name.lower()), args=(obj.pk,))
        except NoReverseMatch:
            return None
        return link
    else:
        return None


@register.inclusion_tag('tags/version_indicator.html', takes_context=True)
def gipsy_version_indicator(context, location, css_classes=None):
    context['display_version_indicator'] = False
    if VERSION_INDICATOR and VERSION_INDICATOR_LOCATION == location:
        context['version_label'], context['version_description'] = \
            VERSION_INDICATOR
        context['display_version_indicator'] = True

        if css_classes is not None:
            context['css_classes'] = css_classes

    return context
