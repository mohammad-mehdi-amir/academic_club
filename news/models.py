from django.db import models
from accounts.models import User

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title