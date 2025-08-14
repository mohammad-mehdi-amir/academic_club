from django.db import models
from accounts.models import User

class News(models.Model):
    STATUS_CHOICES = (
        ('draft','پیش‌نویس'),
        ('published','منتشر شده'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_news')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    
    
    
    