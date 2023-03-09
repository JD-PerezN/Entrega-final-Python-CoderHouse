from django.urls import path
from django.contrib.auth.views import LogoutView

from AppBlog import views

urlpatterns = [
    path("", views.PostList.as_view(), name="appblog-inicio"),
    path("detalle/<slug:slug>", views.post_detail, name="appblog-detalle"),
    path("creacion/", views.PostCreate.as_view(), name="appblog-creacion"),
    path("login/", views.login_request, name="appblog-login"),
    path("logout/", LogoutView.as_view(template_name="AppBlog/post-logout.html"), name="appblog-logout"),
    path("eliminar/<slug:slug>", views.PostDelete.as_view(), name="appblog-eliminar"),
    path("editar/<slug:slug>", views.PostUpdate.as_view(), name="appblog-editar"),
    path("agregar-avatar/", views.agregar_avatar, name="appblog-avatar"),
    path("editar-perfil/", views.editar_perfil, name="appblog-perfil"),
    path("crear-usuario/", views.register_username, name="appblog-create")
]