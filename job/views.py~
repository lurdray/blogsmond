from django.shortcuts import render, get_object_or_404
from .models import Job, Scholarship
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy


# Create your views here.
def PostJobView(request):
	if request.method == "POST":
		title = request.POST.get("title")
		company = request.POST.get("company")
		location = request.POST.get("location")
		description = request.POST.get("description")
		how_to_a = request.POST.get("how_to_a")
		deadline = request.POST.get("deadline")
		poster = request.POST.get("poster")
		pub_date = timezone.now()
		image = request.FILES["image"]
		
		job = Job.objects.create(title=title, company=company, location=location, description=description, how_to_a=how_to_a, deadline=deadline, poster=poster, image=image, pub_date=pub_date, slug=title)
		job.save()
		return HttpResponseRedirect(reverse("post_job"))
		
	else:
		return render(request, 'job/post_job.html')


def PostScholarshipView(request):
	if request.method == "POST":
		institution = request.POST.get("institution")
		course = request.POST.get("course")
		requirement = request.POST.get("requirement")
		link = request.POST.get("link")
		country = request.POST.get("country")
		benefit = request.POST.get("benefit")
		description = request.POST.get("description")
		how_to_a = request.POST.get("how_to_a")
		deadline = request.POST.get("deadline")
		poster = request.POST.get("poster")
		pub_date = timezone.now()
		image = request.FILES["image"]
		
		sch = Scholarship.objects.create(institution=institution, course=course, requirement=requirement, link=link,   country=country, benefit=benefit, description=description, how_to_a=how_to_a, deadline=deadline, poster=poster, image=image, pub_date=pub_date, slug=institution)
		sch.save()
		return HttpResponseRedirect(reverse("post_scholarship"))
		
	else:
		return render(request, 'job/post_scholarship.html')


def AllScholarshipsView(request):
	scholarships = Scholarship.objects.order_by("-pub_date")
	jobs = Job.objects.order_by("-pub_date")[:6]
	context = {"jobs": jobs, "scholarships": scholarships}
	
	return render(request, "job/all_scholarships.html", context)

def AllJobView(request):
	jobs = Job.objects.order_by("-pub_date")
	scholarships = Scholarship.objects.order_by("-pub_date")[3:10]
	context = {"jobs": jobs, "scholarships": scholarships}
	
	return render(request, "job/all_jobs.html", context)

def JobDetail(request, slug):
	job = get_object_or_404(Job, slug=slug)
	four_jobs = Job.objects.order_by("-pub_date")[:4]
	jobs = obs = Job.objects.order_by("-pub_date")[4:11]
	scholarships = Scholarship.objects.order_by("-pub_date")[3:10]
	
	context = {"job": job, "four_jobs": four_jobs, "jobs": jobs, "scholarships": scholarships}
	
	return render(request, "job/job_detail.html", context)
	
def ScholarshipDetail(request, slug):
	scholarship = get_object_or_404(Scholarship, slug=slug)
	scholarships = Scholarship.objects.order_by("-pub_date")[3:10]
	one_schos = Scholarship.objects.order_by("-pub_date")[1:3]
	jobs = obs = Job.objects.order_by("-pub_date")[2:9]
	context = {"scholarship": scholarship, "scholarships": scholarships, "one_schos": one_schos, "jobs": jobs}
	#context = {"scholarship": scholarship}
	
	return render(request, "job/scholarship_detail.html", context)
