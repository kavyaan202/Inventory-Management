# inventory/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item

class ItemTests(APITestCase):

    def setUp(self):
        self.item_data = {'name': 'Test Item', 'description': 'Test Description', 'quantity': 10}

    def test_create_item(self):
        response = self.client.post(reverse('item-list'), self.item_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_item_list(self):
        response = self.client.get(reverse('item-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserTests(APITestCase):

    def setUp(self):
        self.user_data = {'username': 'testuser', 'password': 'testpassword'}

    def test_user_registration(self):
        response = self.client.post(reverse('user-register'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        self.client.post(reverse('user-register'), self.user_data)
        response = self.client.post(reverse('user-login'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
