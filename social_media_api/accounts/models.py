
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', through='Follow')

    def __str__(self):
        return self.username

class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField(auto_now_add=True)

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def follow(self, user):
        """Follow another user."""
        self.following.add(user)

    def unfollow(self, user):
        """Unfollow a user."""
        self.following.remove(user)

    def is_following(self, user):
        """Check if the current user is following another user."""
        return self.following.filter(id=user.id).exists()

    def __str__(self):
        return self.username
