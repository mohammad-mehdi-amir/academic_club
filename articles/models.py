from django.db import models
from accounts.models import User

class Article(models.Model):
    STATUS_CHOICES = (
        ('pending', 'در انتظار بررسی'),
        ('approved', 'تأیید شده'),
        ('rejected', 'رد شده'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title