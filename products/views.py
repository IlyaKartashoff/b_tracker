from django.db.models import Prefetch
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
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