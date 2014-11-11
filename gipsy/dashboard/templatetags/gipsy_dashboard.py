from django import template

from gipsy.dashboard.models import GipsyDashboardMenu
from gipsy.dashboard import settings


register = template.Library()


@register.inclusion_tag('tags/gipsy_dashboard_menu.html', takes_context=True)
def gipsy_dashboard_menu(context, *args, **kwargs):
    """
    This tags manages the display of the admin menu.
    """
    context['items'] = GipsyDashboardMenu.objects.filter(parent__isnull=True)\
        .order_by('order')
    context['dashboard_url'] = settings.GIPSY_DASHBOARD_URL
    context['vanilla_index_url'] = settings.GIPSY_VANILLA_INDEX_URL
    return context


@register.inclusion_tag('tags/widgets/active_users.html')
def dashboard_active_users(count=0, title="CURRENTLY ACTIVE USERS",
                           label="CURRENT USERS"):
    return {'count': count, 'title': title, 'label': label}


@register.inclusion_tag('tags/widgets/item_list.html')
def dashboard_item_list(items, title="MOST RECENT ITEMS"):
    return {'items': items, 'title': title}
