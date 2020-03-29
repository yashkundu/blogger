from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Blog
from .forms import BlogForm

# Create your views here.

class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blogs/blog_form.html'
    fields = ['title', 'content']


class BlogUpdateView(UpdateView):
    model =Blog
    template_name_suffix = '_update_form'
    fields = ['title', 'content']


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:list')
