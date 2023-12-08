from django.shortcuts import render

from django.views.generic import ListView
from posts.models import Posts


# Create your views here.

class PostListView(ListView):
    queryset = Posts.objects.all()
    template_name = './posts/posts.html'
    context_object_name = 'posts'
