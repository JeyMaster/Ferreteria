from django.contrib import admin
from django import forms
from core.sistema.models import *

# Register your models here.
	
class ProductsAdmin(admin.ModelAdmin):
	fields=('product_name','unit_price','category_id'
	,'supplier_id','picture','discontinued')
	list_display=('product_name','unit_price','units_in_stock','category_id'
	,'supplier_id','picture','units_on_order','discontinued')
	list_filter=('category_id',)
	search_fields=['product_name']

	
class CategoriesAdmin(admin.ModelAdmin):
	list_display=('category_id','category_name','description')

class SuppliersAdmin(admin.ModelAdmin):
	list_display=('company_name','contact_name','address','city',
	'postal_code','country','phone')

class OrdersAdmin(admin.ModelAdmin):
	
	list_display=('order_id','customer_name','user_id','order_date')
	list_filter=('order_id','user_id','order_date')
	search_fields=('customer_name',)

class OrderDetailsAdmin(admin.ModelAdmin):

	list_display=('order_id','product_id','unit_price','quantity','discount')
	search_fields=('order_id',)
	list_filter=('order_id',)
	

admin.site.register(Orders,OrdersAdmin)
admin.site.register(OrderDetails,OrderDetailsAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(Suppliers,SuppliersAdmin)
admin.site.register(Categories,CategoriesAdmin)