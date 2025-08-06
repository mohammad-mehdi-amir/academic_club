from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import User
# Register your models here.

@admin.register(User)
class CustomuserAdmin(ModelAdmin):
    list_display=['username','role']