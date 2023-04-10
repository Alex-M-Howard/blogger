from django.urls import path
from . import views

urlpatterns = [
  path('', views.all_blogs, name='all_blogs'),
  path('my_blogs', views.my_blogs, name='my_blogs'),
  path('add_blog', views.add_blog, name='add_blog'),
]