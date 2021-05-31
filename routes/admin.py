from django.contrib import admin

from routes.models import Route


class RouteAdmin(admin.ModelAdmin):
    class Meta:
        model = Route
    list_display = ('id', 'name', 'from_city', 'to_city', 'travel_times')
    list_editable = ['from_city', 'name']


admin.site.register(Route, RouteAdmin)
