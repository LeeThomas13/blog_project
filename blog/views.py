from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blog

class BlogListView():
    template_name = 'blog-list.html'
    model = Blog

class BlogDetailView():
    template_name = 'blog-detail.html'
    model = Blog

class BlogCreateView():
    template_name = 'blog-create.html'
    model = Blog

class BlogUpdateView():
    template_name = 'blog-update.html'
    model = Blog

class BlogDeleteView():
    template_name = 'blog-delete.html'
    model = Blog




