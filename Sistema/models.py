from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User
# Create your models here.

class Suppliers(models.Model):
	supplier_id=models.AutoField(primary_key=True)
	company_name=models.CharField(max_length=40)
	contact_name=models.CharField(max_length=40)
	address=models.CharField(max_length=60,null=True)
	city=models.CharField(max_length=15,null=True)
	postal_code=models.CharField(max_length=10,null=True)
	country=models.CharField(max_length=15,null=True)
	phone=models.CharField(max_length=24,null=True)
	class Meta:
		verbose_name_plural='Suppliers'
	
	def __str__(self):
		return self.company_name
	

class Categories(models.Model):
	class Meta:
		verbose_name_plural='Categories'

	category_id=models.AutoField(primary_key=True)
	category_name=models.CharField(max_length=15)
	description=models.TextField(null=True)

	def __str__(self):
		return self.category_name
	
	

class Products(models.Model):
	product_id=models.AutoField(primary_key=True)
	product_name=models.CharField(max_length=50,null=False)
	supplier_id=models.ForeignKey('Suppliers',on_delete=models.CASCADE)
	category_id=models.ForeignKey('Categories',on_delete=models.CASCADE)
	picture=models.ImageField(upload_to='products/',null=True,blank=True)
	unit_price=models.DecimalField(decimal_places=2,max_digits=5)
	units_in_stock=models.IntegerField(null=True)
	units_on_order=models.IntegerField(null=True)
	discontinued=models.BooleanField(default=False)

	def __str__(self):
		return self.product_name

	class Meta:
		verbose_name_plural='Products'


class Orders (models.Model):

	order_id=models.AutoField(primary_key=True)
	customer_name=models.CharField(max_length=40)
	user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	order_date = models.DateTimeField()


	def __str__(self):
		return repr(self.order_id)

	class Meta:
		verbose_name ='Order'
		verbose_name_plural ='Orders'

class OrderDetails(models.Model):
	order_id=models.ForeignKey(Orders,on_delete=models.CASCADE)
	product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
	unit_price=models.DecimalField(max_digits=5,decimal_places=2)
	quantity = models.SmallIntegerField()
	discount = models.DecimalField(max_digits=5, decimal_places=2)
	

	def __str__(self):
		return repr(self.order_id)

	class Meta:
		verbose_name = 'Order_Detail'
		verbose_name_plural = 'Order_Details'