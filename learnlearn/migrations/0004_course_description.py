# Generated by Django 3.0.2 on 2020-01-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnlearn', '0003_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=None),
        ),
    ]
