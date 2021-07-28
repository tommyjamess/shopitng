from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'date', 'time', 'rating', 'image', 'intro', 'body', 'slug',)
    prepopulated_fields = {'slug': ('title',)}

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'resp', 'date', 'time', 'name', 'active', )




admin.site.register(Post, PostAdmin)
admin.site.register(Response, ResponseAdmin )