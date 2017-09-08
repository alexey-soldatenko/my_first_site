# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('url_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('context', models.TextField()),
                ('date_publicate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name_part', models.CharField(max_length=100, default='other')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='part',
            field=models.ForeignKey(to='articles.Part'),
        ),
    ]
