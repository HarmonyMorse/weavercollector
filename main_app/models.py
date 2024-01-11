from django.db import models
from django.urls import reverse


# Create your models here.
class Weaver(models.Model):
    alias = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    universe = models.CharField(max_length=50)
    enemies = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"weaver_id": self.id})
