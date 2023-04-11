from django.shortcuts import render
from .models import BlogPost, Comment, BlogPostForm, CommentForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'all_blogs.html')
  
def user_blogs(request):
    # user_id = request.user.id
    return render(request, 'my_blogs.html')
    
def add(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return HttpResponseRedirect('/blog/')
    else: 
        form = BlogPostForm()
        
    return render(request, 'add_blog.html', {'form': form})