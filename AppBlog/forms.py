from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppBlog import models

## Create your forms here
# Comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('name', 'email', 'body')

# Avatar form
class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = models.Avatar
        fields = "__all__"
        exclude = ["user"]

# User form
class UserEditForm(forms.Form):

    username = forms.CharField(label="Nombre de usuario")
    email = forms.EmailField(label="Correo")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

# Creation user form
class MyUserCreationForm(UserCreationForm):

    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        help_texts = {k: "" for k in fields}