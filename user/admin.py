from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'image', 'email', 'address', 'phone', 'city', 'country']
    # readonly_fields = ['username', 'first_name', 'last_name', 'image', 'email', 'address', 'phone', 'city', 'country']


admin.site.register(UserProfile, UserProfileAdmin)
