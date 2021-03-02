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
