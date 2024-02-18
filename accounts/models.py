from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(null=True)
    email = models.EmailField(null=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.user.username
