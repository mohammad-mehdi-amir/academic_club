from django.contrib import admin
from .models import EventRegistration,Event
from django.contrib.admin import ModelAdmin
# Register your models here.
@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display=[ 
    'title',
    'description',
    'date',
    'created_by',
    'created_at']
    
    
@admin.register(EventRegistration)
class EventRegistrationAdmin(ModelAdmin):
    list_display=[     'user',
    'event',
    'registered_at',]