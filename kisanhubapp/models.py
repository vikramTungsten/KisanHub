import django
from django.db import models


# Create your models here.


class Regions(models.Model):
    region = models.CharField(max_length=100, null=False, blank=False)
    created_by = models.CharField(max_length=100, blank=False, null=False)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(default=django.utils.timezone.now)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(str(self.region))


class DataType(models.Model):
    datatype = models.CharField(max_length=100, null=False, blank=False)
    created_by = models.CharField(max_length=100, blank=False, null=False)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(default=django.utils.timezone.now)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(str(self.datatype))


class DataDownloadLinks(models.Model):
    region = models.ForeignKey(Regions, null=False, blank=False)
    datatype = models.ForeignKey(DataType, null=False, blank=False)
    link=models.CharField(max_length=500, blank=False, null=False)
    created_by = models.CharField(max_length=100, blank=False, null=False)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(default=django.utils.timezone.now)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(str(self.region) + str(self.datatype))


class Data(models.Model):
    datadownload = models.ForeignKey(DataDownloadLinks, null=False, blank=False)
    year = models.CharField(max_length=50, null=False, blank=False)
    jan = models.CharField(max_length=50, null=True, blank=True)
    feb = models.CharField(max_length=50, null=True, blank=True)
    mar = models.CharField(max_length=50, null=True, blank=True)
    apr = models.CharField(max_length=50, null=True, blank=True)
    may = models.CharField(max_length=50, null=True, blank=True)
    jun = models.CharField(max_length=50, null=True, blank=True)
    jul = models.CharField(max_length=50, null=True, blank=True)
    aug = models.CharField(max_length=50, null=True, blank=True)
    sep = models.CharField(max_length=50, null=True, blank=True)
    oct = models.CharField(max_length=50, null=True, blank=True)
    nov = models.CharField(max_length=50, null=True, blank=True)
    dec = models.CharField(max_length=50, null=True, blank=True)
    win = models.CharField(max_length=50, null=True, blank=True)
    spr = models.CharField(max_length=50, null=True, blank=True)
    sum = models.CharField(max_length=50, null=True, blank=True)
    aut = models.CharField(max_length=50, null=True, blank=True)
    ann = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.CharField(max_length=100, blank=False, null=False)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(default=django.utils.timezone.now)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(str(self.datadownload))


