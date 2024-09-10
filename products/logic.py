
from products.models import Products, Group_of_products

def get_group_product_tree():
    """Возвращает словарь групп-продуктов"""
 
    
    group_product_dict = {
    group: products for group in Group_of_products.objects.all()
    if (products := group.products.all())
}
    return group_product_dict