from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms


class Category(models.Model):
    cat = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.cat 
    

    class Meta:
        db_table = 'category'
        managed = True 
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
class Brand(models.Model):
    brand = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.brand 

    class Meta:
        db_table = 'brand'
        managed = True
        verbose_name = 'brand'
        verbose_name_plural = 'brands'



class Product(models.Model):

    AVAILABILITY = (
        ('Instock', 'Instock'),
        ('Out of stock', 'Out of stock')
    )

    cat = models.ForeignKey(Category, on_delete= models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE)
    prod_name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.SmallIntegerField()
    amount = models.IntegerField(null=True, blank=True)
    product_id = models.CharField(max_length=20, null=True, blank=True)
    availability = models.CharField(max_length=20, choices= AVAILABILITY, default='Instock')
    HDD = models.CharField(max_length=50, null=True, blank=True)
    processor = models.CharField(max_length=200, null=True, blank=True)
    RAM = models.CharField(max_length=40, blank=True, null=True)
    screen_size = models.CharField(max_length=50, null=True, blank=True)
    featured = models.BooleanField(blank=True)
    recommended = models.BooleanField(blank=True)
    condition = models.CharField(max_length=20, default= 'New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.prod_name 

    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=225)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'review'
        managed = True
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

        



# class Review(models.Model):
#     prod = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
#     rev = RichTextUploadingField(blank=True)
#     date = models.DateField(auto_now_add=True)
#     time = models.TimeField(auto_now_add=True)
#     name = models.CharField(max_length=30)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return 'Review by {} on {}'.format(self.name, self.prod)

    
# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model  = Review
#         fields = ('rev', 'name')
    



