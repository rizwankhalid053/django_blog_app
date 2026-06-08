from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 🔴 CHANGED THIS LINE: Swapped ImageField for CharField to bypass Pillow
    image = models.CharField(max_length=255, default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'