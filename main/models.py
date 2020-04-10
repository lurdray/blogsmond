from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Comment(models.Model):
	name = models.CharField(max_length=50)
	comment = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.name
		
class Vote(models.Model):
	name = models.CharField(max_length=50)
	comment = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.name
		


class Blog(models.Model):
    title = models.CharField(max_length=250)
    blogger = models.CharField(max_length=25, default="blogsmond")
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blogs/images/')
    body = models.TextField()
    comments = models.ManyToManyField(Comment, through="BlogCommentConnector")
    votes = models.ManyToManyField(Vote, through="BlogVoteConnector")
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
    	self.slug = slugify(self.title)
    	super().save(*args, **kwargs)
    	
    def get_absolute_url(self):
    	return "/blog/%s/"%self.slug
    	
    def __str__(self):
    	return self.title
  
  

  
class BlogCommentConnector(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default="")
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)

class BlogVoteConnector(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default="")
	vote = models.ForeignKey(Vote, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)

