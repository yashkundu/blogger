from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django import forms
from django.forms.utils import ErrorList

from django.urls import reverse_lazy
from .models import Blog
from .forms import BlogForm

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UpdatePermissionMixin

from django.db.models import Q

# Create your views here.

class BlogListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Blog

    def get_queryset(self):
        user = self.request.user
        qs = Blog.objects.filter(Q(author__in=user.profile.get_following()) | Q(author=user)).order_by('-timestamp')
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter( Q(title__icontains=query) | Q(content__icontains=query)).distinct()
        return qs


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blogs/blog_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(BlogCreateView, self).form_valid(form)
        form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must to logged in to create a Blog.'])
        return self.form_invalid(form)



class BlogUpdateView(UpdatePermissionMixin, UpdateView):
    model =Blog
    template_name_suffix = '_update_form'
    fields = ['title', 'content']


class BlogDeleteView(UpdatePermissionMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:list')
