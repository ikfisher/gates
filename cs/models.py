from django.db import models

class author(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=32)

class paper(models.Model):
    title = models.CharField(max_length=128)
    authors= models.ManyToManyField(author)

