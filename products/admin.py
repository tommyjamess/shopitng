from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', 'slug',)
    prepopulated_fields = {'slug': ('cat',)}


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'slug',)
    prepopulated_fields = {'slug': ('brand',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', 'brand', 'prod_name', 'image', 'price', 'product_id', 'availability', 'HDD', 'processor', 'RAM', 'screen_size', 'featured', 'recommended', 'condition', 'created_at', 'updated_at', 'slug',)
    prepopulated_fields = {'slug': ('prod_name',)}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'comment', 'rate', 'created_at',)





admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
