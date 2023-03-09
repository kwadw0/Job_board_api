from django.contrib import admin
from .models import Job, Applicant, Application, Employer

admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(Application)
admin.site.register(Employer)

# Register your models here.
