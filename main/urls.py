from django.urls import path
# from products.views import GroupListView, ProductListView
from main.views import IndexView
app_name = 'main'

urlpatterns = [
    #path('', IndexView.as_view(), name='index'),
    #path('products/', ProductListView.as_view(), name='products'),

]