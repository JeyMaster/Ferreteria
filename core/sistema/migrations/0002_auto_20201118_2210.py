# Generated by Django 3.1.3 on 2020-11-18 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='suppliers',
            options={'verbose_name': 'Supplier', 'verbose_name_plural': 'Suppliers'},
        ),
        migrations.AlterModelTable(
            name='categories',
            table='Categories',
        ),
        migrations.AlterModelTable(
            name='orderdetails',
            table='Order_details',
        ),
        migrations.AlterModelTable(
            name='orders',
            table='Orders',
        ),
        migrations.AlterModelTable(
            name='products',
            table='Products',
        ),
    ]
