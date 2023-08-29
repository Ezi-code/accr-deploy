from django.shortcuts import render
from .models import Blog, Categories, RescentPost, HomeBlogs



# Create your views here.
def home(request):
    categories = Categories.objects.all()
    blogs = HomeBlogs.objects.all()
    rescents = RescentPost.objects.all()
    # for blog in blogs:
    #     print(blog.picture.file)
    context = {
        "blogs":blogs,
        "categories":categories,
        "rescents":rescents,
    }
    return render(request, 'app/home.html', context)



def sport(request):
    
    # if request.method == "GET":
    #     blogs = Blog.objects.filter(category__name=category).first()
    

    # categories = Categories.objects.all()
   
    context = {
        # "categories": categories,
        # "blogs": blogs,
        # "contents": contents,
    }
    # print(blogs)
    return render(request, 'app/sport.html')





def groups(request, category):
    categories  = Categories.objects.all()
    rescents = RescentPost.objects.all()
    blogs = Blog.objects.filter(category__name=category)
    # print(blogs)
    context = { 
        "categories":categories,
        "blogs":blogs,
        "rescents":rescents,
        "category":category 
    }
    return render(request, "app/categories.html", context)


def read_blog(request, title):
    if request.method == 'GET':
        blog = Blog.objects.get(title=title)
        rescents = RescentPost.objects.all()
        categories = Categories.objects.all()
    context = {
        "blog":blog,
        "rescents":rescents,
        "categories":categories
    }
    return render(request, "app/read_blog.html", context)

