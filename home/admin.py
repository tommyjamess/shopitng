from django.contrib import admin
from .models import *

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
     list_display=('id', 'title', 'keywords', 'description', 'company', 'address', 'phone', 'email', 'facebook', 'instagram', 'twitter',  'status','icon','logo', 'default_pic', 'menu_icon', 'created_at', 'updated_at', 'about', 'about', 'contact',)
     list_display_links = ['id','title', 'company' ]


class Banner_oneAdmin(admin.ModelAdmin):
     list_display = ('id', 'image', 'banner_text',)

class Banner_twoAdmin(admin.ModelAdmin):
     list_display = ('id', 'image1', 'image2', 'image3', 'banner_text',)

class Banner_threeAdmin(admin.ModelAdmin):
     list_display = ('id', 'image1', 'image2', 'image3', 'banner_text',)

class UpdateMeAdmin(admin.ModelAdmin):
     list_display = ('id', 'email', 'status',)


admin.site.register(Setting, SettingAdmin)
admin. site.register(Banner_one, Banner_oneAdmin)
admin. site.register(Banner_two, Banner_twoAdmin) 
admin. site.register(Banner_three, Banner_threeAdmin)
admin. site.register(UpdateMe, UpdateMeAdmin) 

