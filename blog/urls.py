from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='all_blogs'),
  path('my_blogs/', views.user_blogs, name='user_blogs'),
  path('my_blogs/add', views.add, name='add_blog'),
]