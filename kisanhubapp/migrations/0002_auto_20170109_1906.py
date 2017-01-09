# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kisanhubapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataDownloadLinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=500)),
                ('created_by', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('datatype', models.ForeignKey(to='kisanhubapp.DataType')),
                ('region', models.ForeignKey(to='kisanhubapp.Regions')),
            ],
        ),
        migrations.RemoveField(
            model_name='datadownload',
            name='datatype',
        ),
        migrations.RemoveField(
            model_name='datadownload',
            name='region',
        ),
        migrations.AlterField(
            model_name='data',
            name='datadownload',
            field=models.ForeignKey(to='kisanhubapp.DataDownloadLinks'),
        ),
        migrations.DeleteModel(
            name='DataDownload',
        ),
    ]
