from django.db import models
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField

class Setting(models.Model):
    STATUS =(
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=50, null=True)
    address = models.CharField( max_length=100)
    phone = models.CharField( null=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    icon = models.ImageField(blank=True,null=True,  upload_to='images/')
    logo = models.ImageField(blank=True,null=True, upload_to='images/')
    default_pic = models.ImageField(blank=True,null=True, upload_to='images/')
    menu_icon = models.ImageField(blank=True,null=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    about =RichTextUploadingField(blank=True)
    contact =RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)

    
    def __str__(self):
        return self.title


class Banner_one(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    banner_text = models.CharField(max_length=20)

    def __str__(self):
        return self.banner_text
    

    class Meta:
        db_table = 'banner_one'
        managed = True 
        verbose_name = 'banner_one'
        verbose_name_plural = 'banner_one'
        



class Banner_two(models.Model):
    image1 = models.ImageField(null=True, blank=True, upload_to='images/')
    image2 = models.ImageField(null=True, blank=True, upload_to='images/')
    image3 = models.ImageField(null=True, blank=True, upload_to='images/')
    banner_text = models.CharField(max_length=20)

    def __str__(self):
        return self.banner_text

    class Meta:
        db_table = 'banner_two'
        managed = True 
        verbose_name = 'banner_two'
        verbose_name_plural = 'banner_two'

class Banner_three(models.Model):
    image1 = models.ImageField(null=True, blank=True, upload_to='images/')
    image2 = models.ImageField(null=True, blank=True, upload_to='images/')
    image3 = models.ImageField(null=True, blank=True, upload_to='images/')
    banner_text = models.CharField(max_length=20)

    def __str__(self):
        return self.banner_text

    class Meta:
        db_table = 'banner_three'
        managed = True 
        verbose_name = 'banner_three'
        verbose_name_plural = 'banner_three'


class UpdateMe(models.Model):

    email = models.CharField(blank=True, max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class UpdateMeForm(ModelForm):
    class Meta:
        model= UpdateMe
        fields = [ 'email',]
    