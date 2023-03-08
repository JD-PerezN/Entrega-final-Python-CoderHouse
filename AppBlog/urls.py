from django.urls import path
from django.contrib.auth.views import LogoutView

from AppBlog import views

urlpatterns = [
    #path("", views.inicio, name="inicio"),
    #path("cursos/", views.cursos, name="cursos"),
    #path("profesores/", views.profesores, name="profesores"),
    #path("estudiantes/", views.estudiantes, name="estudiantes"),
    #path("entregables/", views.entregables, name="entregables"),
    ##path("curso-formulario/", views.curso_formulario, name="curso-formulario"),
    ##path("profesor-formulario/", views.profesor_formulario, name="profesor-formulario"),
    ##path("busqueda-camada/", views.busqueda_camada, name="busqueda-camada"),
    #path("buscar/", views.buscar, name="buscar"),
    #path("leer-profesores/", views.leer_profesores, name="leer-profesores"),
    #path("eliminar-profesor/<profesor_id>", views.eliminar_profesor, name="eliminar-profesor"),
    #path("editar-profesor/<profesor_id>", views.editar_profesor, name="editar-profesor")
    path("", views.PostList.as_view(), name="appblog-inicio"),
    #path("detalle/<slug:slug>", views.PostDetail.as_view(), name="appblog-detalle"),
    path("detalle/<slug:slug>", views.post_detail, name="appblog-detalle"),
    path("creacion/", views.PostCreate.as_view(), name="appblog-creacion"),
    path("login/", views.login_request, name="appblog-login"),
    path("logout/", LogoutView.as_view(template_name="AppBlog/post-logout.html"), name="appblog-logout"),
    path("eliminar/<slug:slug>", views.PostDelete.as_view(), name="appblog-eliminar"),
    path("editar/<slug:slug>", views.PostUpdate.as_view(), name="appblog-editar")
]