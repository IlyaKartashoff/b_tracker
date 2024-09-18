
from django.db.models import Prefetch
from products.models import Group_of_products, Products

def get_groups_and_products():
    """Получение групп и продуктов"""
 
    products = Products.objects.all()
    groups = Group_of_products.objects.prefetch_related(
        Prefetch('products_objects', queryset=products, to_attr='all_products')
    )

    ungrouped_products = products.filter(group__isnull=True)
    tree_for_view = {group: group.all_products for group in groups}
    return tree_for_view, ungrouped_products


def add_product():
    pass