from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import User, Profile

@admin.register(User)
class CustomuserAdmin(ModelAdmin):
    list_display = ['username', 'role']

    def get_readonly_fields(self, request, obj=None):
 
        if not (request.user.role == 'admin' or request.user.is_superuser == True):
            return ['role']  
        return []

    def has_change_permission(self, request, obj=None):
        
        if obj and obj != request.user and request.user.role != 'admin':
            return False
        return True


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ['user', 'bio', 'avatar']

    def has_change_permission(self, request, obj=None):
       
        if obj and obj.user != request.user and request.user.role != 'admin':
            return False
        return True