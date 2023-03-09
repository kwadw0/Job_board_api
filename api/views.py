from django.shortcuts import render
from rest_framework import generics
from job.models import Job, Applicant, Application, Employer
from .serializers import JobSerializer, ApplicantSerializer, ApplicationSerializer, EmployerSerializer


class JobApiView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class ApplicantApiView(generics.ListAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class ApplicationApiView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class  EmployerApiView(generics.ListAPIView):
    queryset =  Employer.objects.all()
    serializer_class = EmployerSerializer


# Create your views here.
