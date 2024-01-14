from django.contrib import admin
from shop_link.models import Link, Product


@admin.action(description="Очисить задолженность перед поставщиком")
def make_published(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Link)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status_link', 'name', 'debt')
    list_filter = ('city',)
    actions = [make_published]


@admin.register(Product)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
