from django.contrib import admin
from django.db.models import QuerySet
from network.models import Link, Product
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'create_data')
    list_display_links = ['name', 'model']
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'debt', 'create_data', 'view_provider_link')
    list_filter = ('city',)
    list_display_links = ['name']
    actions = ['clear_debt']
    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debt(self, request, qs: QuerySet):
        qs.update(debt=0.0)
    def view_provider_link(self, obj):
        from django.utils.html import format_html
        url = (
            reverse("admin:network_link_changelist")
            + "?"
            + urlencode({"link__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} </a>', url, obj.provider)
    view_provider_link.short_description = "Ссылка на поставщика"
