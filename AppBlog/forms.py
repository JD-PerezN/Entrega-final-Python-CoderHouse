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