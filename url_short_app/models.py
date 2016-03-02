from django.db import models
from django.utils import timezone


class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    shortened = models.CharField(max_length=10)


class Click(models.Model):
    bookmark = models.ForeignKey(Bookmark)
    created = models.DateField(timezone.now())
    accessed = models.DateField(null=True)
    access_count = models.IntegerField(default=0)
