from django.contrib import admin

# Register your models here.

from . models import Jop
from . models import Category

admin.site.register(Jop)
admin.site.register(Category)