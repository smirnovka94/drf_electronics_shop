from django.contrib import admin
from shop_link.models import Link, Contact, Product


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email',)
    list_filter = ('city',)


@admin.action(description="Очисить задолженность перед поставщиком")
def make_published(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Link)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status_link', 'name', 'debt')

    actions = [make_published]


@admin.register(Product)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
