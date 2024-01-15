from django.core.management import BaseCommand

from shop_link.models import Link


class Command(BaseCommand):
    """
    Класс звеньев торговой сети.
    """
    def handle(self, *args, **kwargs):
        link_list = [
            {
                "status_link": "FA",
                "name": "IE",
                "email": "fabric1@mail.ru",
                "country": "Canada",
                "city": "Vancouver",
                "street": "Canada st",
                "num_house": "46D"
            },
            {
                "status_link": "RN",
                "name": "Chaine",
                "email": "chaine@mail.ru",
                "country": "Russia",
                "city": "Moscow",
                "street": "Первая ул",
                "num_house": "4",
                "debt": 10000,
                "related_link": Link.objects.get(pk=1)
            },
            {
                "status_link": "IE",
                "name": "Socolov",
                "email": "socolov@mail.ru",
                "country": "USA",
                "city": "NY",
                "street": "Three line",
                "num_house": "10",
                "debt": 1541,
                "related_link": Link.objects.get(pk=2)
            },
            {
                "status_link": "IE",
                "name": "Tincoff",
                "email": "tincoff@mail.ru",
                "country": "Russia",
                "city": "Yfa",
                "street": "Tincoff st",
                "num_house": "100",
                "related_link": Link.objects.get(pk=2)
            },
            {
                "status_link": "RN",
                "name": "retail",
                "email": "retail@mail.ru",
                "country": "USA",
                "city": "Uta",
                "street": "Uta ул",
                "num_house": "4",
                "debt": 5555,
                "related_link": Link.objects.get(pk=4)
            },
        ]

        link_for_create = []
        for link_item in link_list:
            link_for_create.append(
                Link(**link_item)
            )

        Link.objects.bulk_create(link_for_create)
        print(link_for_create)
