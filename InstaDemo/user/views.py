from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from user.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from .models import *
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HelloDjango(TemplateView):
    template_name="home.html"


class PostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name="post.html"
    login_url='login'


class PostDetailView(DetailView):
    model = Post
    template_name="post_detail.html"


class PostCreateView(CreateView):
    model=Post
    template_name="make_post.html"
    fields="__all__"


class PostUpdateView(UpdateView):
    model=Post
    template_name="update_post.html"
    fields=("title",)


class PostDeleteView(DeleteView):
    model=Post
    template_name="delete_post.html"
    success_url=reverse_lazy("home")


class SignupView(CreateView):
    form_class=CustomUserCreationForm
    template_name="signup.html"
    success_url=reverse_lazy("login")