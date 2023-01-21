from django.db import models
import uuid
class Project(models.Model):
    # owner =
    title = models.CharField(max_length=200, )
    description = models.TextField(null=True, max_length=1000, blank=True,)
    # futured_img =
    demo_link = models.CharField(null=True, max_length=1000, blank=True,)
    source_link = models.CharField(null=True, max_length=1000, blank=True,)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tags', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    TAG_TYPE = (
        ('up', 'up'),
        ('down', 'down'),
    )
    # owner =
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE,)
    body = models.TextField(max_length=200, null=True, blank=True,)
    value = models.CharField(max_length=50, choices=TAG_TYPE,)
    update = models.DateTimeField(auto_now=True,)
    created = models.DateTimeField(auto_now_add=True,)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False,)

    def __str__(self):
        return self.value


class Tags (models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False, )

    def __str__(self):
        return self.name





