from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from AppBlog import models
from AppBlog import forms

### Create your views here.
## VIEWS BASED ON CLASSES
# VIEW TO SEE THE LIST OF POST
class PostList(ListView):

    queryset = models.Post.objects.filter(status=1).order_by("-created_on")
    template_name = "AppBlog/post-list-index.html"

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

#def register(req):
#    if req.method == "POST":
#        form = forms.MyUserCreationForm(req.POST)

#        if form.is_valid():
#            username = form.cleaned_data["username"]
#            contexto = {"mensaje": "usuario creado"}
#            return render(req, "AppBlog/post-list-index.html", contexto)
    
#    else:
#        form = forms.MyUserCreationForm()
#        contexto = {"form": form}
#        return render(req, "AppBlog/user-create.html", contexto)
    
# View to login in the website
def login_request(req):

    form = AuthenticationForm()

    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

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

# View to see all comments in posts
def post_detail(request, slug):
    template_name = 'AppBlog/post-detail-index.html'
    post = get_object_or_404(models.Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = forms.CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

# View to update avatar picture
@login_required
def agregar_avatar(req):
    avatar = req.user.avatar
    mi_formulario = forms.AvatarFormulario(instance=avatar)

    if req.method == "POST":
        mi_formulario = forms.AvatarFormulario(req.POST, req.FILES, instance=avatar)
        if mi_formulario.is_valid():
            mi_formulario.save()

            return redirect("/")
    
    else:
        return render(req, "AppBlog/avatar-create.html", {"mi_formulario": mi_formulario})

# View to update an existing user logged in website   
@login_required
def editar_perfil(req):
    usuario = User.objects.get(username=req.user)

    if req.method == "POST":
        mi_formulario = forms.UserEditForm(req.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            usuario.username = informacion["username"]
            usuario.email = informacion["email"]
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]    

            usuario.save()

            return redirect("/")
    
    else:
        mi_formulario = forms.UserEditForm(initial={"username": usuario.username,
                                              "email": usuario.email,
                                              "last_name": usuario.last_name,
                                              "first_name": usuario.first_name})
        
    return render(req, "AppBlog/user-update.html", {"mi_formulario": mi_formulario})

# View to create a new user in the website
def register_username(req):

    if req.method == "POST":
        form = forms.MyUserCreationForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            contexto = {"mensaje": "Usuario creado satisfactoriamente"}
            return render(req, "AppBlog/post-list-index.html", contexto)
        
    else:
        form = forms.MyUserCreationForm()
        contexto = {"form": form}
        return render(req, "AppBlog/user-create.html", contexto)