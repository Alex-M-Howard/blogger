from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
