from django.urls import reverse
from django.test import TestCase, Client

from products import models
from products.base import Languages, ProductType


class TestHomeView(TestCase):

    url = reverse('home')

    def test_successful_response(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        product = models.Product.objects.create(
            name='Test product',
            product_type=ProductType.BOOSTER_BOX,
            language=Languages.ENGLISH,
        )
        response = self.client.get(self.url)
        self.assertEqual(list(response.context['latest_products']), [product])


class TestProductTypeView(TestCase):

    url = reverse(
        'product-by-type',
        kwargs={'product_type': ProductType.SINGLE_CARD}
    )

    def test_successful_response(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_bad_product_type(self):
        bad_url = reverse(
            'product-by-type',
            kwargs={'product_type': 'fake-product-type'}
        )
        response = self.client.get(bad_url)
        self.assertEqual(response.status_code, 404)

    def test_context_includes_product_correct_type(self):
        product = models.Product.objects.create(
            name='Test product',
            product_type=ProductType.SINGLE_CARD,
            language=Languages.ENGLISH,
        )
        response = self.client.get(self.url)
        self.assertEqual(list(response.context['product_type']), [product])

    def test_context_excludes_product_incorrect_type(self):
        product = models.Product.objects.create(
            name='Test product',
            product_type=ProductType.BOOSTER_BOX,
            language=Languages.ENGLISH,
        )
        response = self.client.get(self.url)
        self.assertEqual(list(response.context['product_type']), [])


class TestDetailView(TestCase):

    def test_successful_response(self):
        # Add a product
        response = self.client.get(reverse('detail', kwargs={'id': product.id}))
        self.assertEqual(response.status_code, 200)

    def test_bad_id(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


class TestSearchView(TestCase):

    def test_successful_response(self):
        # Not sure how to do query string params in reverse. I think it's something like
        # url = reverse('search') + 'q=charizard'
        response = self.client.get('/search/?q=charizard')
        self.assertEqual(response.status_code, 200)

    def test_context_includes_product_correct_search(self):
        product = models.Product.objects.create(
            name='Test product',
            product_type=ProductType.BOOSTER_BOX,
            language=Languages.ENGLISH,
        )
        response = self.client.get('/search/?q=Test')
        self.assertEqual(list(response.context['product_list']), [product])

    def test_context_excludes_product_incorrect_search(self):
        pass