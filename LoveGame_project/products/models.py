from django.db import models

class Product(models.Model):
    id          = models.Number()
    name        = models.TextField()
    image       = models.TextField()
    desciption  = models.TextField()