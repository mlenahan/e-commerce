from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from products import models
from django.http import Http404
from django.shortcuts import get_object_or_404
from products.models import ProductType, Product
from django.db.models import Q

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

    def get_context_data(self, product_type=None):
        if product_type not in [c[0] for c in ProductType.CHOICES]:
            raise Http404()
        context = super().get_context_data()
        context['product_type'] = (
            models.Product.objects.filter(product_type=product_type)
            .order_by('-created_at')
        )
        return context

class ProductDetailView(TemplateView):

    template_name = 'product_detail_view.html'

    def get_context_data(self, id=None):
        context = super().get_context_data()
        context['product'] = get_object_or_404(models.Product, id=id)
        return context


class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(Q(name__icontains=query))
        return object_list



