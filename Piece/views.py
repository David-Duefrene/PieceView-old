from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.decorators import login_required

#from .forms import CreatePiece
from .models import Post

@login_required
class PostCreate(CreateView): #FormView):
    model = Post
    fields = ['title', 'body']

