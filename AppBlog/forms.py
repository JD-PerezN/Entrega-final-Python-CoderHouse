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