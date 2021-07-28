from django.contrib import admin
from .models import ShopCart, Order

# Register your models here.


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_code', 'user', 'product', 'quantity', 'price', 'amount', 'order_placed')
    list_filter = ('user',)
    list_display_link = ('product',)
    readonly_fields = ('order_code', 'user', 'product', 'quantity', 'price', 'amount', 'order_placed' )
    can_delete = False


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_placed', 'prodname', 'payment_code', 'first_name', 'last_name', 'address', 'city', 'state', 'country', 'email', 'total', 'phone', 'status', 'created_at',)
    list_filter = ('status',)
    list_display_link = ('user',)
    readonly_fields = ( 'order_placed', 'payment_code', 'total', 'created_at', 'user', 'city', 'state', 'country', 'email', 'phone', )
    can_delete = False 


admin.site.register(ShopCart, ShopCartAdmin) 
admin.site.register(Order, OrderAdmin) 