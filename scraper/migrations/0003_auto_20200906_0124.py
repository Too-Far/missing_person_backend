# Generated by Django 3.1.1 on 2020-09-06 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_auto_20200905_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='id_number',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
