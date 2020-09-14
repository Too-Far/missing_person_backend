from rest_framework import serializers
from scraper.models import MissingPerson

class MissingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissingPerson
        fields = ('first_name', 'id_number', 'last_name', 'current_age',
                'age_when_missing', 'gender', 'height', 'weight', 'ethnicity',
                'eye_color', 'hair_color', 'circumstances', 'agency_name',
                'agency_zip', 'agency_address', 'agency_city', 'agency_state',
                'thumbnail_url', 'case_qr_code', 'date_reported', 'agency_website')
