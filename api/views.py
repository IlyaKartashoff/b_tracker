from rest_framework import permissions, viewsets
from api.serializers import CategoriesSerializer, ProductsSerializer, GroupsSerializer
from products.models import Products, Categories, Group_of_products

class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group_of_products.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [permissions.IsAuthenticated] 
