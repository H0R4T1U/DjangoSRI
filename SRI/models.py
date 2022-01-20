from django.db import models

# Create your models here.
class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    container_class = models.CharField(max_length=50)
    classes = models.CharField(max_length=200)
