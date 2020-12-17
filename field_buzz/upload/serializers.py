from rest_framework import serializers
from .models import UploadInfo

class UploadInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadInfo
        fields = ( 'name',
                   'email',
                   'phone',
                   'full_address',
                   'name_of_university',
                    'graduation_year',
                    'cgpa',
                    'experiment_in_month',
                    'current_work_place_name',
                    'applying_in',
                    'expected_salary',
                    'applying_in',
                    'field_buzz_reference',
                    'github_project_url',
                  )