# Generated by Django 2.1.3 on 2019-11-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
