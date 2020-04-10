from django.shortcuts import render, get_object_or_404
from .models import Blog
from job.models import Job, Scholarship
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Create your views here.

def PostBlogView(request):
	if request.method == "POST":
		title = request.POST.get("title")
		pub_date = timezone.now()
		image = request.FILES["image"]
		body = request.POST.get("body")
		blogger = request.POST.get("blogger")
		
		blog = Blog.objects.create(title=title, body=body, image=image, blogger=blogger, pub_date=pub_date, slug=title)
		blog.save()
		return HttpResponseRedirect(reverse("post_blog"))
		
	else:
		return render(request, 'main/post_blog.html')
	

def about(request):
	context = {}
	return render(request, "main/about.html", context)
	
def AllBlogsView(request):
	blogs = Blog.objects.order_by("-pub_date")
	jobs = Job.objects.order_by("-pub_date")[3:10]
	scholarships = Scholarship.objects.order_by("-pub_date")[3:10]
	context = {"blogs": blogs, "jobs": jobs, "scholarships": scholarships}
	return render(request, "main/all_blogs.html", context)
	
def index(request):
	latest_blog = Blog.objects.order_by("-pub_date")[:1]
	two_blogs = Blog.objects.order_by("-pub_date")[1:3]
	three_blogs = Blog.objects.order_by("-pub_date")[3:6]
	four_jobs = Job.objects.order_by("-pub_date")[:7]
	blogs = 	Blog.objects.order_by("-pub_date")[6:]
	scholarships = Scholarship.objects.order_by("-pub_date")[:11]

	context = {"latest_blog": latest_blog, "two_blogs": two_blogs, "three_blogs": three_blogs, "four_jobs": four_jobs, "blogs": blogs, "scholarships": scholarships}
	
	return render(request, 'main/index.html', context)
	
def blog_detail(request, slug):
	blog = get_object_or_404(Blog, slug=slug)
	
	
	blogs = Blog.objects.order_by("-pub_date")[1:3]
	second_blogs = Blog.objects.order_by("-pub_date")[2:3]
	jobs = Job.objects.order_by("-pub_date")[3:10]
	scholarships = Scholarship.objects.order_by("-pub_date")[3:10]
	
	context = {"blog": blog, "blogs": blogs, "second_blogs": second_blogs, "jobs": jobs, "scholarships": scholarships}
	return render(request, "main/blog_detail.html", context)
	#return HttpResponse(slug)
	#return HttpResponse(f'sjdsdsdsdcsdcsdcsdc {slug}')
	

