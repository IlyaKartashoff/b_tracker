
from django.db import models

# class Group_of_products(models.Model):
#     name = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name

class Products(models.Model):

    # LENGTH_CHOICES = [
    #     (20, '20 cm'),
    #     (30, '30 cm'),
    #     (40, '40 cm'),
    #     (50, '50 cm'),
    #     (60, '60 cm'),
    #     (70, '70 cm'),
    #     (80, '80 cm'),
    #     (100, '100 cm'),
    #     (110, '110 cm'),
    #     (120, '120 cm'),
    #     (130, '130 cm'),
    #     (140, '140 cm'),
    #     (150, '150 cm'),
    # ]
    
    name = models.CharField('Наименование продукта',max_length=100, unique=True)
    # colour = models.CharField(max_length=100, blank=True, null=True)
    # size = models.IntegerField(choices=LENGTH_CHOICES)
    # quantity = models.PositiveIntegerField(blank=True, null=True)
    # group = models.ForeignKey(to=Group_of_products(), related_name='products',
    #                            on_delete=models.CASCADE, blank=True, null=True)
    # image = models.ImageField(upload_to='product_photos/', blank=True)
    # purchase_prise = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, blank=True, null=True)
    # sale_prise = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

