from django.shortcuts import render
from .models import Blog, Image


def home(request):
    blogs = Blog.objects.all()[0:9]
    context = {
        'blogs':blogs
    }
    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contact.html')

def blog(request, post_name):
    blog_name = post_name.replace('-', ' ')
    blog = Blog.objects.get(title=blog_name)
    image = Image.objects.get(blog_id=blog.id)
    return render(request, 'blog.html', {'blog':blog, 'image_url':image.image.url})