# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('context', models.TextField()),
                ('user_name', models.CharField(max_length=100)),
                ('article_name', models.CharField(max_length=50)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
