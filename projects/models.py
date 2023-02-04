
from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
     # owner=
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, max_length=200)
    # futured_img
    demo_link = models.CharField(null=True, blank=True, max_length=1000)
    source_link = models.CharField(null=True, blank=True, max_length=1000)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
