import uuid
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

def custom_validate_email(value):
    if "@abc.com" in value:
        raise ValidationError('Email format is incorrect')


class UploadInfo(models.Model):
    #tsync_id = models.CharField(primary_key=True, max_length=55, blank=False, unique=True, default=uuid.uuid4, editable=False)
    name =  models.CharField(max_length=256, blank=False)
    email = models.EmailField(max_length=256, blank=False, unique=False, validators=[validate_email])
    phone = models.CharField(max_length=14, blank=False)
    full_address = models.CharField(max_length=512, blank=False)
    name_of_university = models.CharField(max_length=256, blank=False)
    graduation_year = models.IntegerField(blank=False,validators=[
            MaxValueValidator(2020),
            MinValueValidator(2015)
        ])
    cgpa = models.FloatField(blank=True, null=True, validators=[
            MaxValueValidator(4.0),
            MinValueValidator(2.0)
        ]) 
    experiment_in_month = models.IntegerField(blank=True, validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    CHOICES = (
        ('M', 'Mobile'),
        ('B', 'Backend'),
    )
    current_work_place_name = models.CharField(max_length=256, blank=True)
    applying_in = models.CharField(max_length= 2, choices = CHOICES, blank=False)
    expected_salary = models.IntegerField(blank=False, validators=[
            MaxValueValidator(60000),
            MinValueValidator(15000)
        ])
    field_buzz_reference = models.CharField(max_length=256, blank=True)
    github_project_url = models.URLField(max_length = 512, blank=False) 
    ### cv
    
    ##
    #on_spot_update_time = models.DateTimeField(auto_now=True)
    #on_spot_creation_time = models.DateTimeField(auto_now=True, auto_now_add=False,editable=False)
    
    
    def __str___(self):
        return self.name



###
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)