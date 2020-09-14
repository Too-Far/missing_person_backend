# Generated by Django 3.1.1 on 2020-09-06 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missingperson',
            name='age_now',
        ),
        migrations.RemoveField(
            model_name='missingperson',
            name='agency_phone',
        ),
        migrations.RemoveField(
            model_name='missingperson',
            name='agency_web',
        ),
        migrations.RemoveField(
            model_name='missingperson',
            name='city_last_seen',
        ),
        migrations.RemoveField(
            model_name='missingperson',
            name='date_last_seen',
        ),
        migrations.RemoveField(
            model_name='missingperson',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='missingperson',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='missingperson',
            name='l_name',
        ),
        migrations.AddField(
            model_name='missingperson',
            name='agency_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='agency_city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='agency_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='agency_state',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='agency_zip',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='case_qr_code',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='circumstances',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='current_age',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='ethnicity',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='eye_color',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='gender',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='hair_color',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='height',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='id_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='thumbnail_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='weight',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='age_when_missing',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
