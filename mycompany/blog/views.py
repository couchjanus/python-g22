from django.shortcuts import render

from django.views.generic import TemplateView
from .models import Post
from django.views.generic import ListView, DetailView

class HomeView(TemplateView):
    template_name = "blog/index.html"

class PostListView(ListView):  
    model = Post  
    context_object_name = 'posts'  

class PostDetailView(DetailView):
    model = Post
