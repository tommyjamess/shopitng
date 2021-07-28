from django.db import models

from django.contrib.auth.models import User

from django.forms import ModelForm
from products.models import Product
from django.forms import Select

class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True )
    quantity = models.IntegerField(blank=True, null=False)
    order_code = models.CharField(max_length=70, editable=False)
    order_placed = models.BooleanField(default=False)


    def __str__(self):
        return self.product.prod_name
    

    @property
    def price(self):
        if self.product_id is not None:
            return (self.product.price)

 
    @property
    def amount(self):
        if self.product_id is None:
            return (None)
        else:
            if self.product.price:
                return(self.product.price * self.quantity)

class ShopCartForm(ModelForm):
    class Meta:
        models = ShopCart
        fields = ['quantity', 'size']




class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Onshipping', 'Onshippong'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )


    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    prodname = models.CharField(max_length=225, null=True)
    total = models.FloatField(null=True, blank=True)
    order_placed = models.BooleanField(default=False)
    # order_code = models.CharField(max_length=70, editable=False)
    payment_code = models.CharField(max_length=8, editable=False)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=30, null=True)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField( blank=True, max_length=20)
    state = models.CharField(blank=True, null=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    status = models.CharField(max_length=10, choices=STATUS, default='new')
    adminnoted = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.user.username
    

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [ 'first_name', 'last_name', 'address', 'email', 'phone',  'city', 'country']

