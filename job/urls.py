
from django.urls import path
from . import views

#app_name = "job"

urlpatterns = [
	path("alljobs/", views.AllJobView, name="all_jobs"),
	path("allscholarships/", views.AllScholarshipsView, name="all_scholarships"),
	path("job/<slug:slug>/", views.JobDetail, name="job_detail"),
	path("scholarship/<slug:slug>/", views.ScholarshipDetail, name="scholarship_detail"),
	path("postjob/", views.PostJobView, name="post_job"),
	path("postscholarship/", views.PostScholarshipView, name="post_scholarship"),
]
