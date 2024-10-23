
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, UpdateView
from products.models import Group_of_products, Products
from products.logic import get_groups_and_products
from common.views import TitleMixin


# class GroupListView(ListView):
#     model = Group_of_products
#     template_name = 'main/products.html'
#     context_object_name = 'groups'

class GroupCreateView(TitleMixin, CreateView):
    """Создает грппу товаров"""
    title = 'Создание группы'
    template_name = 'products/create_group.html'
    model = Group_of_products
    fields = [
        'name',
        'parent'
    ]
    success_url = reverse_lazy('products:products_list')

class ProductTreeListView(TitleMixin, TemplateView):
    """Отображает список товаров по группам"""
    template_name = 'products/products.html'
    title = 'Список продуктов'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tree, ungrouped_products = get_groups_and_products()

        context['tree'] = tree
        context['ungrouped_products'] = ungrouped_products
        return context

class ProductCreateView(TitleMixin,CreateView):
    """Создает новый продукт"""
    title = "Создание товара"
    model = Products
    fields = [
        'name', 'group', 'category', 'colour', 'size', 'quantity', 'image', 'purchase_price', 'sale_price'
    ]
    template_name = 'products/create_product.html'
    success_url = reverse_lazy('products:products_list')

    # def form_valid(self, form: BaseModelForm) -> HttpResponse:
    #     #some logic
    #     return super().form_valid(form)

class ProductDetailView(TitleMixin,DetailView):
    """Карточка товара"""
    title = 'Детальная информация'
    model = Products
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

class ProductEditView(TitleMixin, UpdateView):
    """Изменить продукт"""
    title = "Изменить"
    model = Products
    fields = ['name', 'group', 'category', 'colour', 'size', 'quantity', 'image', 'purchase_price', 'sale_price']
    context_object_name = 'edit_object'
    template_name = 'products/product_edit.html'
    success_url = reverse_lazy('products:products_list')

class ProductDeleteView(TitleMixin,DeleteView):
    """Удаляет продукт"""
    title = 'Подтверждение удаления'
    model = Products
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:products_list')
    context_object_name = 'delete_object'
