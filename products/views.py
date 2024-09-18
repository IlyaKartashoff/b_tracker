
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView
from products.models import Group_of_products, Products
from products.logic import get_groups_and_products
from common.views import TitleMixin


class GroupListView(ListView):
    model = Group_of_products
    template_name = 'main/products.html'
    context_object_name = 'groups'

        
class ProductTreeListView(TitleMixin, TemplateView):
    template_name = 'main/products.html'
    title = 'Список продуктов'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tree, ungrouped_products = get_groups_and_products()

        context['tree'] = tree
        context['ungrouped_products'] = ungrouped_products
        return context

# class ProductCreateView(TitleMixin,CreateView):
#     title = "Создание товара"
#     model = Products
#     fields = [
#         'name', 'group', 'category', 'colour', 'size', 'quantity', 'image', 'purchase_price', 'sale_price'
#     ]
#     template_name = 'products/create_product.html'
#     success_url = reverse_lazy('products_list')

#     def form_valid(self, form: BaseModelForm) -> HttpResponse:
#         return super().form_valid(form)
