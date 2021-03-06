from django.shortcuts import render
from .models import Post
from django.views.generic import ListView




# Create your views here.

def Home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/Home.html', context)


class  PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    


def about(request):
    return render(request, 'blog/about.html', {'title':'About'} )

