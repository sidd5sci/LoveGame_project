from django.contrib import admin

# Register your models here.
from .models import *

admin.site.Register(Product)
admin.site.Register(Categories)
