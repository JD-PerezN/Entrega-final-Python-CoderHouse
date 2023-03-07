from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from AppBlog import models

## Create your views here.
# VIEW TO SEE THE LIST OF POST
class PostList(ListView):

    queryset = models.Post.objects.filter(status=1).order_by("-created_on")
    template_name = "AppBlog/post-list.html"

# VIEW TO CHECK THE DETAIL OF A PARTICULAR POST
class PostDetail(DetailView):

    model = models.Post
    template_name = "AppBlog/post-detail.html"