from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment, BlogCommentConnector
#from job.models import Job, Scholarship
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
		keywords = request.POST.get("keywords")
		
		blog = Blog.objects.create(title=title, body=body, image=image, blogger=blogger, keywords=keywords, pub_date=pub_date, slug=title)
		blog.save()
		return HttpResponseRedirect(reverse("post_blog"))
		
	else:
		return render(request, 'main/post_blog.html')
	

def about(request):
	context = {}
	return render(request, "main/about.html", context)
	
def AllBlogsView(request):
	blogs = Blog.objects.order_by("-pub_date")
	#jobs = Job.objects.order_by("-pub_date")[3:10]
	#scholarships = Scholarship.objects.order_by("-pub_date")[3:10]
	
	#stats
	blog_count = Blog.objects.all()
	comment_count = Comment.objects.all()
	views = 0
	for x in blog_count:
		views += x.views
	#job_count = Job.objects.all()
	#scholarship_count = Scholarship.objects.all()
	
	context = {"blogs": blogs, "blog_count": blog_count, "comment_count": comment_count, "views": views}
	return render(request, "main/all_blogs.html", context)
	
def index(request):
	latest_blog = Blog.objects.order_by("-pub_date")[:1]
	two_blogs = Blog.objects.order_by("-pub_date")[1:3]
	three_blogs = Blog.objects.order_by("-pub_date")[3:6]
	#four_jobs = Job.objects.order_by("-pub_date")[:7]
	blogs = 	Blog.objects.order_by("-pub_date")[6:16]
	#scholarships = Scholarship.objects.order_by("-pub_date")[:11]
	
	#stats
	blog_count = Blog.objects.all()
	comment_count = Comment.objects.all()
	views = 0
	for x in blog_count:
		views += x.views
	#job_count = Job.objects.all()
	#scholarship_count = Scholarship.objects.all()


	context = {"latest_blog": latest_blog, "two_blogs": two_blogs, "three_blogs": three_blogs, "blogs": blogs, "blog_count": blog_count, "comment_count": comment_count, "views": views}
	
	return render(request, 'main/index.html', context)
	
def BlogDetailView(request, slug):
	if request.method == "POST":
		name = request.POST.get("name")
		comment = request.POST.get("comment")
		pub_date = timezone.now()
		comment = Comment.objects.create(name=name, comment=comment, pub_date=pub_date)
		comment.save()
		blog = get_object_or_404(Blog, slug=slug)
		bc = BlogCommentConnector(blog=blog, comment=comment, pub_date=pub_date)
		bc.save()
	
		comments = blog.comments.all()
		blogs = Blog.objects.order_by("-pub_date")[1:3]
		second_blogs = Blog.objects.order_by("-pub_date")[2:3]
		#jobs = Job.objects.order_by("-pub_date")[3:10]
		#scholarships = Scholarship.objects.order_by("-pub_date")[3:10]
	
		#stats
		blog_count = Blog.objects.all()
		comment_count = Comment.objects.all()
		views = 0
		for x in blog_count:
			views += x.views
		#job_count = Job.objects.all()
		#scholarship_count = Scholarship.objects.all()
		
		keyword_str = ""
		keyword_list = []
		for keyword in blog.keywords.split(","):
			keyword_str += ("%s,")%(keyword)
			keyword_list.append(keyword)
	
		context = {"blog": blog, "blogs": blogs, "second_blogs": second_blogs, "blog_count": blog_count, "comment_count": comment_count, "keyword_list": keyword_list, "keyword_str": keyword_str, "views": views, "comments": comments}
		return render(request, "main/blog_detail.html", context)	
		
	else:
		blog = get_object_or_404(Blog, slug=slug)
		blog.views = blog.views + 1
		blog.save()
		comments = blog.comments.all()
		blogs = Blog.objects.order_by("-pub_date")[1:3]
		second_blogs = Blog.objects.order_by("-pub_date")[2:3]
		#jobs = Job.objects.order_by("-pub_date")[3:10]
		#scholarships = Scholarship.objects.order_by("-pub_date")[3:10]
	
		#stats
		blog_count = Blog.objects.all()
		comment_count = Comment.objects.all()
		views = 0
		for x in blog_count:
			views += x.views
		#job_count = Job.objects.all()
		#scholarship_count = Scholarship.objects.all()
		
		keyword_str = ""
		keyword_list = []
		for keyword in blog.keywords.split(","):
			keyword_str += ("%s,")%(keyword)
			keyword_list.append(keyword)
	
		context = {"blog": blog, "blogs": blogs, "second_blogs": second_blogs, "blog_count": blog_count, "comment_count": comment_count, "keyword_list": keyword_list, "keyword_str": keyword_str, "views" :views, "comments": comments}
		return render(request, "main/blog_detail.html", context)	















































#from django.shortcuts import render, get_object_or_404
#from .models import Etc, Comment, EtcCommentConnector
#from django.utils import timezone
#from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import reverse, reverse_lazy

#import random
#from django.db.models import Max, Min

# Create your views here.  https://buildforcovid19.io/corona-virus-symptom-analysis-checker/
#def JoinContestView(request):
#	if request.method == "POST":
#		company_name = request.POST.get("company_name")
#		company_address = request.POST.get("company_address")
#		phone_num = request.POST.get("phone_num")
#		about_company = request.POST.get("about_company")
#		company_type = request.POST.get("company_type")
#		first_comment = request.POST.get("first_comment")
#		second_comment  = request.POST.get("second_comment")
#		third_comment = request.POST.get("third_comment")
#		image = request.FILES["image"]
#		first_image = request.FILES["first_image"]
#		second_image = request.FILES["second_image"]
#		third_image = request.FILES["third_image"]
#		tale = request.POST.get("tale")
#		pub_date = timezone.now()

#		etc = Etc.objects.create(full_name=full_name, company_name=company_name, company_address=company_address, phone_num=phone_num, about_company=about_company, company_type=company_type, first_comment=first_comment, second_comment=second_comment, third_comment=third_comment,  image=image, first_image=first_image,  second_image=second_image, third_image=third_image, tale=tale, pub_date=pub_date, slug=phone_number)
#		etc.save()
		
#		slug = etc.slug
			
		#return HttpResponseRedirect(reverse("contestant_detail"))
#		return HttpResponseRedirect(reverse("contestant_detail", args=(slug,)))
	
#	else:
#		return render(request, 'etc/join_etc.html')

		
		
		
	
def ContestantDetailView(request, slug):
	if request.method == "POST":
		name = request.POST.get("name")
		comment = request.POST.get("comment")
		pub_date = timezone.now()
		comment = Comment.objects.create(name=name, comment=comment, pub_date=pub_date)
		comment.save()
		etc = get_object_or_404(Etc, slug=slug)
		ec = EtcCommentConnector(etc=etc, comment=comment, pub_date=pub_date)
		ec.save()

		etc = Etc.objects.get(slug=slug)
		highest_ten = Etc.objects.order_by("-pub_date")
		comments = etc.comments.all()
		comment_count = comments.count

	
		context = {"etc": etc, "highest_ten": highest_ten, "comments": comments, "comment_count": comment_count, "views": views}
		return render(request, 'etc/c_detail.html', context)


		
		
	else:
		etc = Etc.objects.get(slug=slug)
		etc.views = etc.views + 1
		etc.save()
		highest_ten = Etc.objects.order_by("-pub_date")
		comments = etc.comments.all()
		comment_count = comments.count
	
		context = {"etc": etc, "highest_ten": highest_ten, "comments": comments, "comment_count": comment_count}
		return render(request, 'etc/c_detail.html', context)	

	

def IndexView(request):
	if request.method == "POST":
		phone_num = request.POST.get("phone_num")
		
		etc = get_object_or_404(Etc, phone_num=phone_num)
		slug = etc.slug
		return HttpResponseRedirect(reverse("contestant_detail", args=(slug,)))
		
		
	else:
		random_six = set()
		highest_ten = Etc.objects.all().aggregate(Max('views'))
		#highest_ten = Etc.objects.annotate(min_price=Min('views'), max_price=Max('views'))
		#highest_ten = Etc.objects.order_by("-pub_date")
		etcs = Etc.objects.all()
		try:
			for i in range(4):
				#random_six.add(random.choice(etcs))
				pass
		except:
			pass
				
		
		latest_eight = Etc.objects.order_by("-pub_date")[0]
	
		context = {"highest_ten": highest_ten, "random_six": random_six, "latest_eight": latest_eight}
		return render(request, 'etc/index.html', context)
		#return HttpResponse("hurrayyyyyyy!")
	
	
