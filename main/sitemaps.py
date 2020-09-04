from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Blog
#from job.models import Job, Scholarship
#from anonymous_app.models import Anonymous
#from etc.models import Etc, Post

class StaticViewSitemap(Sitemap):
	changefreq = "always"
	
	def items(self):
		return ["index", "about", "etc"]#, "coronavirustest", "anonymous_app", "etc"]
		
	def location(self, item):
		return reverse(item)


class BlogSitemap(Sitemap):
	
	def items(self):
		return Blog.objects.all()
		#return "asasas"
		

#class JobSitemap(Sitemap):
	
#	def items(self):
#		return Job.objects.all()
		#return "asasas"
		
#class ScholarshipSitemap(Sitemap):
	
#	def items(self):
#		return Scholarship.objects.all()
		#return "asasas"
		
		
#class AnonymousSitemap(Sitemap):
	
#	def items(self):
#		return Anonymous.objects.all()
		#return "asasas"
		
		
		
#class EtcSitemap(Sitemap):
	
#	def items(self):
#		return Etc.objects.all()
		#return "asasas"
		
		
		
#class EtcBlogSitemap(Sitemap):
	
#	def items(self):
#		return Post.objects.all()
		#return "asasas"
		
		
		
		
