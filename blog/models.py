from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=225)
    date = models.DateField()
    time = models.TimeField()
    rating = models.SmallIntegerField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    intro = RichTextUploadingField(blank=True)
    body = RichTextUploadingField(blank=True, null=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        managed = True
        verbose_name = 'post'
        verbose_name_plural = 'post'


class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='responses')
    resp = RichTextUploadingField(blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Response by {} on {}'.format(self.name, self.post)

    
class ResponseForm(forms.ModelForm):
    class Meta:
        model  = Response
        fields = ('resp', 'name')




