from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from ..admin import GipsyMenu, ChildrenInline
from .models import GipsyDashboardMenu


class ChildrenDashboardInline(ChildrenInline):
    model = GipsyDashboardMenu
    exclude = ('icon', 'content_type', )


class GipsyDashboardMenuAdmin(GipsyMenu):
    inlines = [ChildrenDashboardInline]
    exclude = ('url', 'parent', 'content_type', )

    def save_formset(self, request, form, formset, change):
        """
        Populates the content type before saving the inline objects.
        """
        super(GipsyDashboardMenuAdmin, self).save_formset(request, form, formset, change)
        for item in formset:
            if not 'id' in item.cleaned_data or not item.cleaned_data['id']:
                continue
            instance = item.cleaned_data['id']
            if instance.url == item.cleaned_data['url']:
                continue

            instance.url = item.cleaned_data['url']
            url_args = instance.get_url_args()
            if url_args:
                i = 0
                while i < len(url_args):
                    url = None
                    try:
                        url = reverse('admin:%s_%s_add' % (url_args[i], url_args[i+1]))
                    except:
                        pass
                    if url:
                        try:
                            instance.content_type = ContentType.objects.get(app_label=url_args[i], model=url_args[i+1])
                            instance.save()
                        except ContentType.DoesNotExist:
                            pass
                    i += 1

admin.site.register(GipsyDashboardMenu, GipsyDashboardMenuAdmin)
