from django.urls import path
from products.views import GroupListView, ProductListView

app_name = 'main'

urlpatterns = [
    path('', GroupListView.as_view(), name='index'),
    path('', ProductListView.as_view(), name='products'),

]