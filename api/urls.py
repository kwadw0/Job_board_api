from django.urls import path
from .views import JobApiView, ApplicantApiView, ApplicationApiView, EmployerApiView

urlpatterns = [
    path('', JobApiView.as_view()),
    path('applicant/', ApplicantApiView.as_view()),
    path('application/', ApplicationApiView.as_view()),
    path('employer', EmployerApiView.as_view())
]