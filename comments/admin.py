from django.contrib import admin
from .models import Comment
from django.contrib.admin import ModelAdmin

@admin.register(Comment)
class CommemntAdmin(ModelAdmin):
    list_display=['author',
    'content',
    'created_at',
    'content_type',
    'object_id',
    'content_object']