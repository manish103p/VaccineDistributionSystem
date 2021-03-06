# Generated by Django 3.1.5 on 2021-03-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine_app', '0004_auto_20210330_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districtvaccinedata',
            name='arrivalTimestamp',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='districtvaccinedata',
            name='departureTimestamp',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='vaccinelot',
            name='departureTimestamp',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
