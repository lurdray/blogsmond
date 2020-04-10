from django.db import models
from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Job(models.Model):
	title = models.CharField(max_length=250)
	company = models.CharField(max_length=250)
	location = models.CharField(max_length=250)
	description = models.CharField(max_length=250)
	how_to_a = models.CharField(max_length=250)
	deadline = models.CharField(max_length=250)
	image = models.ImageField(upload_to='jobs/images/')
	pub_date = models.DateTimeField(default=timezone.now)
	poster = models.CharField(max_length=25, default="blogsmond")
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)
		
	def get_absolute_url(self):
		return "/job/%s/"%self.slug
		#return f'/{self.slug}/'
	
	def __str__(self):
		return self.title
		
		
		
		
class Scholarship(models.Model):
	institution = models.CharField(max_length=250)
	course = models.CharField(max_length=250)
	requirement = models.CharField(max_length=250)
	link = models.CharField(max_length=250)
	country = models.CharField(max_length=250)
	benefit = models.CharField(max_length=250)
	description = models.CharField(max_length=250)
	how_to_a = models.CharField(max_length=250)
	image = models.ImageField(upload_to='scholarships/images/')
	deadline = models.CharField(max_length=250)
	pub_date = models.DateTimeField(default=timezone.now)
	poster = models.CharField(max_length=25, default="blogsmond")
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.institution)
		super().save(*args, **kwargs)
		
	def get_absolute_url(self):
		return "/scholarship/%s/"%self.slug
		#return f'/{self.slug}/'
	
	def __str__(self):
		return self.institution
