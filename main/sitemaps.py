from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Blog
from job.models import Job, Scholarship

class StaticViewSitemap(Sitemap):
	changefreq = "always"
	
	def items(self):
		return ["index", "about"]
		
	def location(self, item):
		return reverse(item)


class BlogSitemap(Sitemap):
	
	def items(self):
		return Blog.objects.all()
		#return "asasas"
		

class JobSitemap(Sitemap):
	
	def items(self):
		return Job.objects.all()
		#return "asasas"
		
class ScholarshipSitemap(Sitemap):
	
	def items(self):
		return Scholarship.objects.all()
		#return "asasas"
