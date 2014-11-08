from django import template

from gipsy.dashboard.models import GipsyDashboardMenu


register = template.Library()


@register.inclusion_tag('tags/gipsy_dashboard_menu.html', takes_context=True)
def gipsy_dashboard_menu(context, *args, **kwargs):
    """
    This tags manages the display of the admin menu.
    """
    context['items'] = GipsyDashboardMenu.objects.filter(parent__isnull=True)\
        .order_by('order')
    return context
