
from products.models import Product
from django.views.generic import TemplateView, ListView


class ProductListView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'