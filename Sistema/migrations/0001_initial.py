# Generated by Django 3.1.1 on 2020-09-11 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=15)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=40)),
                ('contact_name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=60, null=True)),
                ('city', models.CharField(max_length=15, null=True)),
                ('postal_code', models.CharField(max_length=10, null=True)),
                ('country', models.CharField(max_length=15, null=True)),
                ('phone', models.CharField(max_length=24, null=True)),
            ],
            options={
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('units_in_stock', models.IntegerField(null=True)),
                ('units_on_order', models.IntegerField(null=True)),
                ('discontinued', models.BooleanField(default=False)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.categories')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.suppliers')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=40)),
                ('order_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.SmallIntegerField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.orders')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.products')),
            ],
            options={
                'verbose_name': 'Order_Detail',
                'verbose_name_plural': 'Order_Details',
            },
        ),
    ]
