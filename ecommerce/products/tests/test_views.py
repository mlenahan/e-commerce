from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product, ProductItem
import json

class TestViews(TestCase):

    # def set_up(self):
    #     self.client = Client()
    #     self.home_url = reverse('home')


    def test_home_page_view(self):
        self.client = Client()
        response = self.client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')