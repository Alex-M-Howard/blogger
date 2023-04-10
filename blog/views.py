from django.shortcuts import render

# Create your views here.
def all_blogs(request):
    return render(request, 'all_blogs.html')
  
def my_blogs(request):
    return render(request, 'my_blogs.html')
    
def add_blog(request):
    return render(request, 'add_blog.html')