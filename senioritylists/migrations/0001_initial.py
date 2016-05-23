# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 22:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import senioritylists.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('ecrew_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ecrew ID')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeniorityList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='SeniorityListEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_seniority', models.IntegerField(verbose_name='master seniority')),
                ('captain_seniority', models.IntegerField(verbose_name='captain seniority')),
                ('status', models.CharField(max_length=2, validators=[senioritylists.models.validate_status], verbose_name='status')),
                ('pilot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='senioritylists.Pilot')),
                ('seniority_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='senioritylists.SeniorityList')),
            ],
        ),
    ]
