from django.urls import path
from products.views import ProductTreeListView, ProductCreateView, ProductDetailView, ProductDeleteView

app_name = 'products'

urlpatterns = [
    path('', ProductTreeListView.as_view(), name='products_list'),
    path('products/new',ProductCreateView.as_view(), name='product_new'),
    path('products/<int:pk>',ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/delete',ProductDeleteView.as_view(), name='product_delete'),
]
