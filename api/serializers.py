from rest_framework import serializers
from job.models import Job, Applicant, Application, Employer



class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('job_title','job_description','job_type', 
        'job_location', 'job_salary', 'job_posted_date', 
        'job_expiry_date'
        )

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = (
            'employer', 'employer_company_name', 'employer_description',
            'employer_website', 'employer_phone_number'
        )

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = (
            'applicant', 'applicant_resume'
        )


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            'job_id', 'applicant_id', 'application_date'
        )