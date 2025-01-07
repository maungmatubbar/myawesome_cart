from django.contrib import admin
from django.utils.html import format_html

from .models import Product, Contact, Orders


# Register your models here.
#diplay admin panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','image', 'price', 'pub_date')  #
    search_fields = ('product_name',)  # Search bar for the product name
    list_filter = ('pub_date', 'price')  # Filters for date or price
    ordering = ('-pub_date',)  # Order by latest created first
    list_per_page = 10  # Number of items to show per pag

    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{obj.image.url}" width="50" height="50" />', obj.image.url)
        return "No Image"

    image_display.short_description = "Product Image"  # Column title
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
admin.site.register(Orders)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['product_id', 'product_name', 'desc', 'pub_date']