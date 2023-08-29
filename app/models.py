import datetime
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, default=True, null=False)

    def __str__(self):
        return self.name



# BLOGS MODEL
class Blog(models.Model):
    title = models.CharField(max_length=100, default=True, null=False)
    description = models.CharField(max_length=100, default=True, null=False)
    picture = models.ImageField(default=True, null=False, upload_to='uploads/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    content = HTMLField(default='Blog Content', null=False)
    date = models.DateField(blank=False, default=datetime.date.today)
    author = models.CharField(default='Accreal Sports', null=False, max_length=50)


    def __str__(self):
        return f"{self.title}"




# RESCENT BLOGS 
class RescentPost(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.post.title



# HOMEPAGE BLOGS
class HomeBlogs(models.Model):
	blogs = models.ForeignKey(Blog, on_delete=models.CASCADE)
	
	
	def __str__(self):
		return self.blogs.title


# FEATURES POSTS
class FeaturedPosts(models.Model):
	posts = models.ForeignKey(Blog, on_delete=models.CASCADE)


	def __str__(self):
		return self.posts.title
