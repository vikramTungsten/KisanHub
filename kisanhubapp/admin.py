from django.contrib import admin
from kisanhubapp import models

# Register your models here.

admin.site.register(models.Regions)
admin.site.register(models.DataType)
admin.site.register(models.DataDownloadLinks)
admin.site.register(models.Data)
