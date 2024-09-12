from django.urls import path
from products.views import ProductTreeListView
app_name = 'products'

urlpatterns = [
    path('', ProductTreeListView.as_view(), name='products_list'),
]
