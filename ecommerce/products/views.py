from django.views.generic.base import TemplateView

from products import models


class HomePageView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = (
            models.Product.objects.all()
            .order_by('-created_at')
        )[:5]
        return context


class ProductByTypeView(TemplateView):

    template_name = 'product_by_type.html'

    def get_context_data(self, product_type):
        context = super().get_context_data(product_type)
        context['product_type'] = (
            models.Product.objects.filter(product_type)
            .order_by('-created_at')
        )
        return context

