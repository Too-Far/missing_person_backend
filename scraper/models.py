from django.db import models

class MissingPerson(models.Model):

    case_qr_code = models.URLField(null=True)
    thumbnail_url = models.URLField(null=True)
    agency_zip = models.CharField(max_length=200, null=True)
    agency_address = models.CharField(max_length=200, null=True)
    agency_state = models.CharField(max_length=200, null=True)
    agency_city = models.CharField(max_length=200, null=True)
    agency_name = models.CharField(max_length=200, null=True)
    circumstances = models.TextField(null=True, blank=True)
    eye_color = models.CharField(max_length=200, null=True)
    hair_color = models.CharField(max_length=200, null=True)
    ethnicity = models.CharField(max_length=200, null=True)
    weight = models.CharField(max_length=200, null=True)
    height = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    age_when_missing = models.CharField(max_length=200, null=True)
    current_age = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    id_number = models.CharField(max_length=200, null=True, unique=True)
    date_reported = models.CharField(max_length=200, null=True)
    agency_website = models.URLField(null=True)

    def __str__(self):
        name = '{} {}'.format(self.first_name, self.last_name)
        return name
