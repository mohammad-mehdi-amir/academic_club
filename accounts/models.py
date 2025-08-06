
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'کاربر عادی'),
        ('member', 'عضو انجمن'),
        ('admin', 'مدیر انجمن'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"