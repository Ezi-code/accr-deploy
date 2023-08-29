from django.contrib import admin
from .models import Blog, Categories,RescentPost,FeaturedPosts,HomeBlogs


# Register your models here.
admin.site.register(Blog)
admin.site.register(Categories)
admin.site.register(RescentPost)
admin.site.register(FeaturedPosts)
admin.site.register(HomeBlogs)
