from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255,)
    flag = models.CharField(max_length=512)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True)

