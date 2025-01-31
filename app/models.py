from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=200)
    weather = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    g_map = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='destination')


