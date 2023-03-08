from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from AppBlog import models

### Create your views here.
## VIEWS BASED ON CLASSES
# VIEW TO SEE THE LIST OF POST
class PostList(ListView):

    queryset = models.Post.objects.filter(status=1).order_by("-created_on")
    template_name = "AppBlog/post-list-index.html"

# VIEW TO CHECK THE DETAIL OF A PARTICULAR POST
class PostDetail(DetailView):

    model = models.Post
    template_name = "AppBlog/post-detail-index.html"

#VIEW TO CREATE A NEW POST
class PostCreate(LoginRequiredMixin, CreateView):

    model = models.Post
    template_name = "AppBlog/post-create.html"
    success_url = reverse_lazy("appblog-inicio")
    fields = ["title", "slug", "author", "content", "status"]

#VIEW TO DELETE A POST
class PostDelete(LoginRequiredMixin, DeleteView):

    model = models.Post
    template_name = "AppBlog/post-delete.html"
    success_url = reverse_lazy("appblog-inicio")

#VIEW TO EDIT AN EXISTING POST
class PostUpdate(LoginRequiredMixin, UpdateView):

    model = models.Post
    template_name = "AppBlog/post-edit.html"
    success_url = reverse_lazy("appblog-inicio")
    fields = ["title", "slug", "author", "content", "status"]
     
## VIEWS BASED ON FUNCTIONS

def register(req):

    if req.method == "POST":
        form = UserCreationForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            contexto = {"mensaje": "Usuario creado satisfactoriamente"}
            return render(req, "AppBlog/post-list-index.html", contexto)
        
    else:
        form = UserCreationForm()
        contexto = {"form": form}
        return render(req, "AppBlog/post-register.html", contexto)
    
# View to login in the website
def login_request(req):

    form = AuthenticationForm()

    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, email=email, password=contra)

            if user is not None:
                login(req, user)
                contexto = {"mensaje": f'Bienvenido {usuario}'}
                return render(req, "AppBlog/post-list-index.html", contexto)
            else:
                contexto = {"mensaje": f'El usuario {usuario} no existe',
                            "form": form}
                return render(req, "AppBlog/post-login.html", contexto)
        
        else:
            contexto = {"mensaje": 'Los datos son erroneos',
                        "form": form}
            return render(req, "AppBlog/post-login.html", contexto)
    
    contexto = {"form": form}
    return render(req, "AppBlog/post-login.html", contexto)