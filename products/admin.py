from django.contrib import admin
from products.models import Category, Group_of_products, Products


admin.site.register(Products)
admin.site.register(Group_of_products)
admin.site.register(Category)
