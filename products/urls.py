from django.urls import path
from products.views import ProductTreeListView, ProductCreateView, ProductDetailView, ProductDeleteView

app_name = 'products'

urlpatterns = [
    path('', ProductTreeListView.as_view(), name='products_list'),
    path('new/',ProductCreateView.as_view(), name='product_new'),
    path('<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/delete/',ProductDeleteView.as_view(), name='product_delete'),
]
