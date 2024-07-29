
from products.models import Products
from django.views.generic import ListView


class ProductListView(ListView):
    model = Products
    template_name = 'products/index.html'
    context_object_name = 'products'
