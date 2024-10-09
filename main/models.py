from django.db import models
from products.models import Products

class Movements(models.Model):
    """Модель событий (crud)"""
    MOVEMENT_TYPE_CHOICES = [
        ('Продажа', 'Продажа'),
        ('Пополнение', 'Пополнение'),
        ('Создание товара', 'Создание товара'),
    ]
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=50, choices=MOVEMENT_TYPE_CHOICES, default='Движение')
    description = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    quantity_change = models.IntegerField()

    def __str__(self) -> str:
        print(self.created_timestamp, type(self.created_timestamp))
        return f'{self.movement_type} - {self.product.name} - {self.created_timestamp.strftime('%d - %m - %Y, %H:%M')}'

    
