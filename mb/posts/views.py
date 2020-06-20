from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

# Create your views here.
class PostView(ListView):
    model = Post
    

def HomePageView(request):
    return render(request, 'posts/home.html')