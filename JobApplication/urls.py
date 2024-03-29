from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('countries', views.CountryCreateView.as_view(), name='country-create'),
    path('countries/list', views.CountryListView.as_view(), name='country-list'),
    path('countries/list/<int:id>', views.CountryDetailView.as_view(), name='country-update'),
    # path('countries/list/export_pdf', views.countries_list_export_pdf, name='countries-export-pdf'),

    path('jobs', views.JobCreateView.as_view(), name='job-create'),
    path('jobs/list', views.JobListView.as_view(), name='job-list'),
    path('jobs/list/<int:id>', views.JobDetailView.as_view(), name='job-detail'),
    path('jobs/list/export_pdf', views.jobs_list_export_pdf, name='export-pdf'),

    path('jobs/<int:job_id>/apply/', views.JobApplicationView.as_view(), name='apply-job'),
    path('applications/list', views.JobApplicationListView.as_view(), name='application-list'),
    # path('applications/list/<int:id>', views.JobApplicationListViewById.as_view(), name='application-list-by-id'),
    path('applications/list/export_pdf', views.applications_list_export_pdf, name='applications-list-export-pdf'),
    
    path('applications/workexperience/list', views.WorkExperienceListView.as_view(), name='workexperience-list'),
    path('applications/workexperience/list/<int:id>', views.WorkExperienceDetailView.as_view(), name='workexperience-detail'),

    path('applications/education/list', views.FormalEducationListView.as_view(), name='education-list'),
    path('applications/education/list/<int:id>', views.FormalEducationDetailView.as_view(), name='education-detail'),

    path('applications/language/list', views.LanguageSkillsListView.as_view(), name='language-list'),
    path('applications/language/list/<int:id>', views.LanguageSkillsDetailView.as_view(), name='language-detail'),

    path('applications/applicant/list', views.ApplicantListView.as_view(), name='applicant-list'),
    path('applications/applicant/list/<int:id>', views.ApplicantDetailView.as_view(), name='applicant-detail'),
    # path('applications/applicant/list/export_pdf', views.applicants_list_export_pdf, name='applicants-export-pdf'),

    path('applications/ai/results_generate/<int:id>', views.ProcessResumesAPIView.as_view(), name='applicant-ai-list'),
    path('applications/ai/results/<int:id>/list', views.ApplicantResultsListView.as_view(),name='applicant-results-list'),
    path('applications/ai/results/<int:id>/list/export_pdf', views.results_export_pdf, name='applicants-export-pdf'),

    path('applications/ai/applicant/list/<int:id>', views.ProcessResumesAPIView.as_view(), name='applicant-ai-list'),

]
