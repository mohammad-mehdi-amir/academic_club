
from django.contrib import admin
from .models import News
from django.contrib.admin import ModelAdmin
# Register your models here.
@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display=[ 
                      'title',
    'content',
    'created_by',
    'status',
    'created_at',
    'published_at',
    ]
    