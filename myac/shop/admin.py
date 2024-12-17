from django.contrib import admin

# Register your models here.
from .models import Product
admin.site.register(Product)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['product_id', 'product_name', 'desc', 'pub_date']