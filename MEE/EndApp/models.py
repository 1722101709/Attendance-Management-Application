from django.db import models

# Create your models here.
class ABC(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    present = models.BooleanField(default=False)