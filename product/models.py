from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1024)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=255, help_text='image url')

    def __str__(self):
        return self.name

    @property
    def get_absolute_url(self):
        return reverse_lazy('product:detail', args=[int(self.pk)])
