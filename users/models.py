from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, )
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    shot_intro = models.CharField(max_length=300, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_images = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_Github = models.CharField(max_length=200, null=True, blank=True)
    social_Twitter = models.CharField(max_length=200, null=True, blank=True)
    social_YouTube = models.CharField(max_length=200, null=True, blank=True)
    social_Linkdin = models.CharField(max_length=200, null=True, blank=True)
    social_WebSite = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return str(self.name)