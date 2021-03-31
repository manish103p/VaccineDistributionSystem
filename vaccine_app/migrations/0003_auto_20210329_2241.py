# Generated by Django 3.1.5 on 2021-03-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine_app', '0002_auto_20210329_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centervaccinedata',
            name='departureTimestamp',
        ),
        migrations.AlterField(
            model_name='vaccinelot',
            name='status',
            field=models.CharField(choices=[('produced', 'produced'), ('transitToDistrict', 'transitToDistrict'), ('atDistrict', 'atDistrict'), ('transitToCenter', 'transitToCenter'), ('atCenter', 'atCenter'), ('consumed', 'consumed')], default='produced', max_length=20),
        ),
    ]