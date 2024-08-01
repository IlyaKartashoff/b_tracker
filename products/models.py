
from unicodedata import category
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Категория товаров')

    class Meta:
        db_table = 'product_categories'
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class Group_of_products(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Группа товаров')
    

    class Meta:
        db_table = 'groups_of_products'
        verbose_name = 'Группа товаров'
        verbose_name_plural = 'Группы товаров'

    def __str__(self):
        return self.name

class Products(models.Model):

    LENGTH_CHOICES = [
        ('20 cm', '20 cm'),
        ('30 cm', '30 cm'),
        ('40 cm', '40 cm'),
        ('50 cm', '50 cm'),
        ('60 cm', '60 cm'),
        ('70 cm', '70 cm'),
        ('80 cm', '80 cm'),
        ('100 cm', '100 cm'),
        ('110 cm', '110 cm'),
        ('120 cm', '120 cm'),
        ('130 cm', '130 cm'),
        ('140 cm', '140 cm'),
        ('150 cm', '150 cm'),
    ]
    name = models.CharField('Наименование продукта',max_length=100, unique=True)
    group = models.ForeignKey(to=Group_of_products, related_name='products',
                               on_delete=models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING,
                                 blank=True, null=True)
    colour = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=250, choices=LENGTH_CHOICES, default=20)
    quantity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='product_photos/', blank=True)
    purchase_prise = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)
    sale_prise = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'

