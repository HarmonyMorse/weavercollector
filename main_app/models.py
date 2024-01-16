from django.db import models
from django.urls import reverse


class Power(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # Add other Power-related attributes as needed

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("powers_detail", kwargs={"pk": self.id})


# Create your models here.
class Weaver(models.Model):
    alias = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    universe = models.CharField(max_length=50)
    enemies = models.TextField(max_length=250)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"weaver_id": self.id})


class Sighting(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)

    weaver = models.ForeignKey(Weaver, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location} on {self.date}"

    class Meta:
        ordering = ["-date"]
