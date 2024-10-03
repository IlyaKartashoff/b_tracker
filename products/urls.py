from django.urls import path
from products.views import GroupCreateView, ProductTreeListView, ProductCreateView, ProductDetailView, ProductDeleteView, ProductEditView

app_name = 'products'

urlpatterns = [
    path('', ProductTreeListView.as_view(), name='products_list'),
    path('new/',ProductCreateView.as_view(), name='product_new'),
    path('group/new/',GroupCreateView.as_view(), name='group_new'),
    path('<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
    path('delete/<int:pk>/',ProductDeleteView.as_view(), name='product_delete'),
    path('edit/<int:pk>/',ProductEditView.as_view(), name='product_edit'),
]
