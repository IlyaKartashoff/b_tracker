from django.views.generic import ListView, TemplateView
from products.models import Group_of_products, Products
from products.logic import get_group_product_tree
from common.views import TitleMixin


class GroupListView(ListView):
    model = Group_of_products
    template_name = 'main/products.html'
    context_object_name = 'groups'

# class ProductListView(TitleMixin, ListView):
#     model = Products
#     template_name = 'main/products.html'
#     context_object_name = 'products'
#     title = 'Список товаров'


class ProductListView(TitleMixin, TemplateView):
    template_name = 'main/products.html'
    title = 'Список продуктов'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group_of_products.objects.all()
        context['products'] = Products.objects.all()
        context['tree'] = get_group_product_tree()
        return context
         