from django.db import models


# Create your models here.
class Product(models.Model):
    image_url = models.URLField()
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=80, unique=True)
    display_size = models.FloatField()
    cpu = models.CharField(max_length=32)
    gpu = models.CharField(max_length=32)
    ram_size = models.IntegerField()
    rom_size = models.IntegerField()

    def __str__(self):
        return self.name
