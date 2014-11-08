from django.contrib import admin


class ChildrenInline(admin.TabularInline):
    sortable_field_name = "order"


class GipsyMenu(admin.ModelAdmin):
    inlines = [ChildrenInline]
    exclude = ('parent',)
    list_display = ['name', 'order']
    ordering = ['order']

    def queryset(self, request):
        """Overrides default queryset to only display parent items"""
        query = super(GipsyMenu, self).queryset(request)
        return query.filter(parent__isnull=True)
