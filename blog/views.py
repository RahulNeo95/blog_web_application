from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView, DetailView ,UpdateView, DeleteView, CreateView


from rest_framework import generics, permissions
from .serializers import PostSerializer


class BlogListView(ListView):
    template_name='home.html'
    model=Post

class BlogDetailView(DetailView):
    template_name='post_detail.html'
    model=Post

class BlogEditView(UpdateView):
    template_name='post_edit.html'
    model=Post
    fields=['title', 'body']

class BlogDeleteView(DeleteView):
    template_name='post_delete.html'
    model=Post
    success_url=reverse_lazy('home')

class BlogCreateView(CreateView):
    template_name='post_create.html'
    model=Post
    fields=['title','author','body']


class PostAPIListView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes= [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes= [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)








