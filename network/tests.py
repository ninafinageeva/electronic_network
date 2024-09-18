from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from network.models import Link, Product
from users.models import User


class ProductAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test1@test1.ru",
            password='12345'
        )
        """Имитация авторизации пользователя по JWT токену."""
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(
            name="test_product",
            model="test_model",
            create_data="2024-09-15"
        )

    def test_create_product(self):
        """Тестирование создания продукта"""
        data = {
            "name": "test_name",
            "model": "test_model",
            "create_data": "2024-09-15"
        }
        response = self.client.post(
            reverse('network:products-list'),
            data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_product(self):
        """Тестирование вывода списка продуктов"""
        response = self.client.get(
            reverse('network:products-list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        """Тестирование частичного редактирования продукта"""
        updated_data = {
            "model": "Updated model"
        }
        response = self.client.patch(
            reverse('network:products-detail', args=[self.product.id]), updated_data
        )
        self.product.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_product(self):
        """Тестирование редактирования продукта"""
        updated_data = {
            "name": "Test_name",
            "model": "Test_model",
            "create_data": "2024-08-20"
        }
        response = self.client.put(
            reverse('network:products-detail', args=[self.product.id]), updated_data
        )
        self.product.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product(self):
        """Тестирование вывода одного продукта
        """
        response = self.client.get(
            reverse('network:products-detail', args=[self.product.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        """Тестирование удаления продукта"""
        response = self.client.delete(
            reverse('network:products-detail', args=[self.product.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class LinkAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test1@test1.ru",
            password='12345'
        )
        """Имитация авторизации пользователя по JWT токену."""
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(
            name="test_product",
            model="test_model",
            create_data="2024-09-15"
        )
        self.prod = Product.objects.all()
        self.link = Link.objects.create(
            name="test_link",
            email="test1@test1.ru",
            country="test_country",
            city="test_city",
            provider=None,
            debt="7000"
        )
        self.link.save()
        self.link.products.add(*self.prod.values_list("id", flat=True))

    def test_create_link(self):
        """Тестирование создания цепочки сети"""
        data = {
            "name": "test_link",
            "email": "test2@test2.ru",
            "country": "test_country",
            "city": "test_city",
            "products": [self.product.id, ],
            "provider": self.link.id,
            "debt": "7000"
        }
        response = self.client.post(
            reverse('network:network-create'),
            data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_link(self):
        """Тестирование вывода списка цепочек сети"""
        response = self.client.get(
            reverse('network:network-list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_link(self):
        """Тестирование редактирования цепочки сети"""
        updated_data = {
            "country": "Updated country"
        }
        response = self.client.patch(
            reverse('network:network-update', args=[self.link.id]), updated_data
        )
        self.link.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_link(self):
        """Тестирование вывода одной цепочки сети"""
        response = self.client.get(
            reverse('network:network-get', args=[self.link.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_link(self):
        """Тестирование удаления цепочки сети
        """
        response = self.client.delete(
            reverse('network:network-delete', args=[self.link.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
