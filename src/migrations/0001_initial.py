# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('published_at', models.DateTimeField(default=datetime.datetime(2016, 9, 30, 18, 45, 10, 95650, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('published_at', models.DateTimeField(default=datetime.datetime(2016, 9, 30, 18, 45, 10, 94611, tzinfo=utc))),
                ('author', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='src.Post'),
        ),
    ]
