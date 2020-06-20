from django.db import models

# Datatypes
# https://www.webforefront.com/django/modeldatatypesandvalidation.html


class Product(models.Model):
    name        = models.TextField()
    image       = models.TextField()
    desciption  = models.TextField()


class Categories(models.Model):
    name        = models.TextField()
    description = models.TextField()
    parent      = models.IntegerField()
    order       = models.IntegerField()