from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'all_blogs.html')
  
def user_blogs(request):
    # user_id = request.user.id
    return render(request, 'my_blogs.html')
    
def add(request):
    return render(request, 'add_blog.html')