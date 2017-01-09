# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=50)),
                ('jan', models.CharField(max_length=50, null=True, blank=True)),
                ('feb', models.CharField(max_length=50, null=True, blank=True)),
                ('mar', models.CharField(max_length=50, null=True, blank=True)),
                ('apr', models.CharField(max_length=50, null=True, blank=True)),
                ('may', models.CharField(max_length=50, null=True, blank=True)),
                ('jun', models.CharField(max_length=50, null=True, blank=True)),
                ('jul', models.CharField(max_length=50, null=True, blank=True)),
                ('aug', models.CharField(max_length=50, null=True, blank=True)),
                ('sep', models.CharField(max_length=50, null=True, blank=True)),
                ('oct', models.CharField(max_length=50, null=True, blank=True)),
                ('nov', models.CharField(max_length=50, null=True, blank=True)),
                ('dec', models.CharField(max_length=50, null=True, blank=True)),
                ('win', models.CharField(max_length=50, null=True, blank=True)),
                ('spr', models.CharField(max_length=50, null=True, blank=True)),
                ('sum', models.CharField(max_length=50, null=True, blank=True)),
                ('aut', models.CharField(max_length=50, null=True, blank=True)),
                ('ann', models.CharField(max_length=50, null=True, blank=True)),
                ('created_by', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DataDownload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_by', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datatype', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='datadownload',
            name='datatype',
            field=models.ForeignKey(to='kisanhubapp.DataType'),
        ),
        migrations.AddField(
            model_name='datadownload',
            name='region',
            field=models.ForeignKey(to='kisanhubapp.Regions'),
        ),
        migrations.AddField(
            model_name='data',
            name='datadownload',
            field=models.ForeignKey(to='kisanhubapp.DataDownload'),
        ),
    ]
