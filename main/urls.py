from django.urls import path
# from products.views import GroupListView, ProductListView
from main.views import MovesView, MovementsDetailView
app_name = 'main'

urlpatterns = [
    path('', MovesView.as_view(), name='index'),
    path('movement/<int:pk>/', MovementsDetailView.as_view(), name='detail'),
]