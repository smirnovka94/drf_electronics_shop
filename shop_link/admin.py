from django.contrib import admin
from django.utils.html import format_html
from shop_link.models import Link, Product


@admin.action(description="Очисить задолженность перед поставщиком")
def make_published(modeladmin, request, queryset):
    """Кнопка обнуления задолженности перед поставщиком"""
    queryset.update(debt=0)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    """Модель отображения звеньев торговой сети в админ-панели"""
    list_display = ('pk', 'status_link', 'name', 'related_link_link', 'debt')
    list_filter = ('city',)
    actions = [make_published]

    def related_link_link(self, obj):
        """Функция отображения параметра related_link в качестве ссылки"""
        link = obj.related_link
        if link:
            return format_html('<a href="/admin/shop_link/link/{}/change/">{}</a>', link.pk, link.name)
        else:
            return None

    related_link_link.allow_tags = True
    related_link_link.short_description = 'ПОСТАВЩИК'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Модель отображения продуктов сети в админ-панели"""
    list_display = ('pk', 'name',)
