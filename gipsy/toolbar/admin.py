from django.contrib import admin

from .models import GipsyToolbarMenu


class ChildrenInline(admin.TabularInline):
    model = GipsyToolbarMenu
    sortable_field_name = "order"


class GipsyToolbarMenuAdmin(admin.ModelAdmin):
    inlines = [ChildrenInline]
    exclude = ('parent',)
    list_display = ['name', 'order']
    ordering = ['order']

    def queryset(self, request):
        """Overrides default queryset to only display parent items"""
        query = super(GipsyToolbarMenuAdmin, self).queryset(request)
        return query.filter(parent__isnull=True)

admin.site.register(GipsyToolbarMenu, GipsyToolbarMenuAdmin)
