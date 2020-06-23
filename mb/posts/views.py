from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

# Create your views here.
class PostView(ListView):
    model = Post
    

def HomePageView(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    
    return render(request, 'posts/home.html', context)