from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Blog


def blog(request):
    return render(request, "blog/blog.html")

class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['site_name','url']
    success_url = reverse_lazy('Insight')
    template_name_suffix = '_create'

class BlogDetailView(DetailView):
    model = Blog

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('Insight')