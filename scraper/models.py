from django.db import models
from django_random_queryset import RandomManager

class MissingPerson(models.Model):

    objects = RandomManager()
    case_qr_code = models.URLField(max_length=2500, null=True)
    thumbnail_url = models.URLField(max_length=2500, null=True)
    agency_zip = models.CharField(max_length=2000, null=True)
    agency_address = models.CharField(max_length=2000, null=True)
    agency_state = models.CharField(max_length=2000, null=True)
    agency_city = models.CharField(max_length=2000, null=True)
    agency_name = models.CharField(max_length=2000, null=True)
    circumstances = models.CharField(max_length=10000000, null=True)
    eye_color = models.CharField(max_length=2000, null=True)
    hair_color = models.CharField(max_length=2000, null=True)
    ethnicity = models.CharField(max_length=2000, null=True)
    weight = models.CharField(max_length=2000, null=True)
    height = models.CharField(max_length=2000, null=True)
    gender = models.CharField(max_length=2000, null=True)
    age_when_missing = models.CharField(max_length=2000, null=True)
    current_age = models.CharField(max_length=2000, null=True)
    last_name = models.CharField(max_length=2000, null=True)
    first_name = models.CharField(max_length=2000, null=True)
    id_number = models.CharField(max_length=2000, null=True, unique=True)
    date_reported = models.CharField(max_length=2000, null=True)
    agency_website = models.URLField(max_length=2500, null=True)

    def __str__(self):
        name = '{} {}'.format(self.first_name, self.last_name)
        return name
