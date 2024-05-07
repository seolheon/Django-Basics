from django.contrib import admin
from core import models

admin.site.register(models.Animal)
admin.site.register(models.Note)
admin.site.register(models.Product)
admin.site.register(models.Task)