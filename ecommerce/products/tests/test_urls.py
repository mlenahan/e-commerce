from django.urls import reverse
from django.test import TestCase, Client

class TestUrls(TestCase):

    def test_home_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_detail_url(self):
        response = self.client.get(reverse('detail', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_product_type_url(self):
        response = self.client.get('/single-card')
        self.assertEqual(response.status_code, 200)


    def test_search_url(self):
        response = self.client.get('/search/?q=charizard')
        self.assertEqual(response.status_code, 200)


