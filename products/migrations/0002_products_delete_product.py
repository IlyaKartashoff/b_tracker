# Generated by Django 5.0.7 on 2024-07-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Наименование продукта')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]