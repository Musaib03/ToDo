# Generated by Django 3.0.5 on 2021-08-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210806_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='newtask',
            name='Check',
            field=models.BooleanField(default=False),
        ),
    ]
