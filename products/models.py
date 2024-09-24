
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Категория товаров')

    class Meta:
        db_table = 'product_categories'
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class Group_of_products(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Группа товаров')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subgroups')

    class Meta:
        db_table = 'groups_of_products'
        verbose_name = 'Группа товаров'
        verbose_name_plural = 'Группы товаров'

    def __str__(self):
        return self.name

class Products(models.Model):

    LENGTH_CHOICES = [
        ('20 cm', '20 cm'),
        ('40 cm', '40 cm'),
        ('60 cm', '60 cm'),
        ('80 cm', '80 cm'),
        ('100 cm', '100 cm'),
        ('130 cm', '130 cm'),
        ('150 cm', '150 cm'),
    ]
    name = models.CharField('Наименование продукта',max_length=100, unique=True)
    group = models.ForeignKey(to=Group_of_products, related_name='products_objects',
                               on_delete=models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('Categories', on_delete=models.DO_NOTHING,
                                 blank=True, null=True)
    colour = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=250, choices=LENGTH_CHOICES, default=20, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='product_photos/', blank=True)
    purchase_price = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name='Себестоимость')
    sale_price = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name='Цена')

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'

