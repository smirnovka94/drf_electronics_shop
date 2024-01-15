from django.core.management import BaseCommand

from shop_link.models import Product, Link


class Command(BaseCommand):
    """
    Класс продуктов.
    """
    def handle(self, *args, **kwargs):
        product_list = [
            {
                "name": "Product1",
                "model": "Product1@mail.ru",
                "data": "2022-01-21",
                "link": Link.objects.get(pk=1)
            },
            {
                "name": "Product2",
                "model": "Product2@mail.ru",
                "data": "2022-01-21",
                "link": Link.objects.get(pk=1)
            },
            {
                "name": "Product3",
                "model": "Product3@mail.ru",
                "data": "2022-01-21",
                "link": Link.objects.get(pk=2)
            },
            {
                "name": "Product4",
                "model": "Product4@mail.ru",
                "data": "2022-01-21",
                "link": Link.objects.get(pk=4)
            },

        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(product_for_create)
        print(product_for_create)
