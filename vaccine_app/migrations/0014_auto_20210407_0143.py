# Generated by Django 3.1.5 on 2021-04-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine_app', '0013_auto_20210406_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='maxCountPerDate',
            field=models.IntegerField(default=10),
        ),
    ]
