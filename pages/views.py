from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'home.html')
