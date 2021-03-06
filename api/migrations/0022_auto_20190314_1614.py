# Generated by Django 2.1.3 on 2019-03-14 16:14

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20190304_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amounts',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=[], size=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
