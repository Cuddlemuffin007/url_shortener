from django.db import models


class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    shortened = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


class Click(models.Model):
    bookmark = models.ForeignKey(Bookmark)
    accessed = models.DateTimeField(null=True)
    access_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['bookmark']

