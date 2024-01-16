from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status

from shop_link.models import Link, Product
from users.models import User

from pytz import timezone
from datetime import datetime


class LinkTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(
            email='user@test.com',
        )
        # Аутентифицируем клиента с созданным пользователем
        self.client.force_authenticate(user=self.user)
        self.user.set_password('test')
        self.user.save()

        utc = timezone('UTC')
        self.data_create = datetime(2024, 1, 15, 20, 0, 0, tzinfo=utc)

        self.link = Link.objects.create(
            status_link="FA",
            name="IE",
            email="fabric1@mail.ru",
            country="Canada",
            city="Vancouver",
            street="Canada st",
            data_create=self.data_create,
            num_house="46D",
            )
        self.link_next = Link.objects.create(
            status_link="IE",
            name="IE Ivaniov",
            email="ivaniov@mail.ru",
            country="Russia",
            city="Spp",
            street="Nevsky Prospekt",
            data_create=self.data_create,
            related_link=self.link,
            num_house="4",
        )

    def test_create_link(self):
        """Тест создание Звена торговой цепи"""
        data = {
            "status_link": "FA",
            "name": "IE",
            "email": "fabric1@mail.ru",
            "country": "Canada",
            "city": "Vancouver",
            "street": "Canada st",
            "data_create": self.data_create,
            "num_house": "46D"
        }
        response = self.client.post(
            reverse('link:link_create'),
            data=data
        )
        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Link.objects.all().exists()
        )

    def test_get_list(self):
        """Тест чтение списка Звена торговой цепи"""
        response = self.client.get(
            '/link/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_link(self):
        """Тест чтение экземпляра Звена торговой цепи"""

        response = self.client.get(
            reverse('link:link_get', args=[self.link.id]))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_link_update(self):
        """Тест Обновление экземпляра Звена торговой цепи"""
        data = {
            "status_link": "FA",
            "name": "new_IE",
            "email": "new_fabric1@mail.ru",
            "country": "new_Canada",
            "city": "new_Vancouver",
            "street": "new_Canada st",
            "data_create": self.data_create,
            "num_house": "46D"
        }

        response = self.client.patch(
            reverse('link:link_update', args=[self.link.id]),
            data=data
        )
        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_link_delete(self):
        """Тест удаление экземпляра Звена торговой цепи"""

        response = self.client.delete(
            reverse('link:link_delete', args=[self.link.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_valid_related_link(self):
        """Тест на валидность заполнения related_link у Завода"""
        data = {
            "status_link": "FA",
            "name": "IE",
            "email": "fabric@mail.ru",
            "country": "Canada",
            "city": "Vancouver",
            "street": "Canada st",
            "data_create": self.data_create,
            "related_link": self.link.id,
            "num_house": "46D"
        }
        response = self.client.post(
            reverse('link:link_create'),
            data=data
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['У завода не может быть поставщика']}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_valid_debt(self):
        """Тест на валидность заполнения debt у Завода"""
        data = {
            "status_link": "FA",
            "name": "IE",
            "email": "fabric@mail.ru",
            "country": "Canada",
            "city": "Vancouver",
            "street": "Canada st",
            "data_create": self.data_create,
            "debt": 200,
            "num_house": "46D"
        }
        response = self.client.post(
            reverse('link:link_create'),
            data=data
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['У завода не может быть задолженности перед поставщиком']}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_valid_debt_update(self):
        """Тест на валидность обновления debt у Завода"""
        data = {
            "status_link": "IE",
            "name": "IE",
            "email": "fabric@mail.ru",
            "country": "Canada",
            "city": "Vancouver",
            "street": "Canada st",
            "data_create": self.data_create,
            "debt": 200,
            "num_house": "46D"
        }
        response = self.client.patch(
            reverse('link:link_update', args=[self.link_next.id]),
            data=data
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['Вы не можете изменять параметр debt ']}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


class ProductTestCase(APITestCase):
    def setUp(self):
        self.user2 = User.objects.create(
            email='user2@test.com',
        )
        self.client.force_authenticate(user=self.user2)
        self.user2.set_password('test')
        self.user2.save()

        utc = timezone('UTC')
        self.data_create = datetime(2024, 1, 15, 20, 0, 0, tzinfo=utc)

        self.link = Link.objects.create(
            status_link="FA",
            name="IE",
            email="fabric1@mail.ru",
            country="Canada",
            city="Vancouver",
            street="Canada st",
            data_create=self.data_create,
            num_house="46D",
        )
        self.product = Product.objects.create(
            name="product1",
            model="product1@mail.ru",
            data="2022-01-21",
            link=self.link,
        )

    def test_create_product(self):
        """Тест создание продуктов"""
        data = {
            "name": "fabric",
            "model": "fabric@mail.ru",
            "data": "2022-01-21",
            "link": self.link.id,
        }
        response = self.client.post(
            reverse('link:product_create'),
            data=data
        )
        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Product.objects.all().exists()
        )

    def test_get_list(self):
        """Тест чтение списка продуктов"""
        response = self.client.get(
            '/product/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_product(self):
        """Тест чтение экземпляра продуктов"""
        response = self.client.get(
            reverse('link:product_get', args=[self.product.id]))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_product_update(self):
        """Тест Обновление экземпляра продуктов"""
        data = {
            "name": "fabric",
            "model": "fabric@mail.ru",
            "data": "2022-01-21",
            "link": self.link.id,
        }

        response = self.client.patch(
            reverse('link:product_update', args=[self.product.id]),
            data=data
        )
        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_product_delete(self):
        """Тест удаление экземпляра продуктов"""

        response = self.client.delete(
            reverse('link:product_delete', args=[self.product.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
