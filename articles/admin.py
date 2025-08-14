from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Article


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display=['id', 'title', 'content', 'submitted_by', 'status', 'submitted_at']