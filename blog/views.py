from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post
from django.urls import reverse_lazy


# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    # fields = ['title']
    fields = '__all__'  # this set all fields from model


class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']  # we only want to edit title and body of the post!
    template_name = 'post_edit.html'


# reverse_lazy opposed to reverse (in urls) it won't execute url redirect until view has finished deleting the blog post
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
