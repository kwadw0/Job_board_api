from django.db import models
from django.contrib.auth import get_user_model

class Job(models.Model):
    PART_TIME = 'PT'
    FULL_TIME = 'FT'
    REMOTE = 'RE'
    CONTRACT = 'CT'
    job_type_list = [
        (PART_TIME, 'Part Time'), 
        (FULL_TIME,'Full Time'), 
        (REMOTE, 'Remote'), 
        (CONTRACT, 'contract'),
        ]
    job_title = models.CharField(max_length=32)
    job_description = models.TextField()
    job_type = models.CharField(max_length=2, choices= job_type_list,
                                 default=FULL_TIME
        
        )
    job_location = models.CharField(max_length=50)
    job_salary = models.PositiveBigIntegerField()
    job_posted_date = models.DateTimeField(auto_now_add=True)
    job_expiry_date = models.DateField(blank=True)


class Employer(models.Model):
    employer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    employer_company_name = models.CharField(max_length=35)
    employer_description = models.TextField()
    employer_website = models.URLField(blank=True)
    employer_phone_number = models.PositiveBigIntegerField()


class Applicant(models.Model):
    applicant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    applicant_resume = models.FileField(upload_to="resume")


class Application(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)
    Applicants_id = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True, blank=True)
    Application_date = models.DateField(auto_now_add=True)



    
    
# Create your models here.
