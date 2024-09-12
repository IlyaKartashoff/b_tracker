from django.contrib import admin
from products.models import Categories, Group_of_products, Products


admin.site.register(Products)
admin.site.register(Group_of_products)
admin.site.register(Categories)
