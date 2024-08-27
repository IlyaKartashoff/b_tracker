
from django.views.generic import ListView
from common.views import TitleMixin
from products.models import Group_of_products, Products


class GroupListView(ListView):
    model = Group_of_products
    template_name = 'main/index.html'
    context_object_name = 'groups'

class ProductListView(TitleMixin, ListView):
    model = Products
    template_name = 'products/products.html'
    context_object_name = 'products'
    title = 'Список товаров'


