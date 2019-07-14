from django.urls import path
from . import views

urlpatterns=[
    # path("",views.HelloDjango.as_view())
    path("home/",views.PostListView.as_view(),name="home"),
    path("post/<int:pk>/",views.PostDetailView.as_view(),name="post_detail"),
    path("make_post/",views.PostCreateView.as_view(),name="make_post"),
    path("update_post/<int:pk>/",views.PostUpdateView.as_view(),name="update_post"),
    path("delete_post/<int:pk>/",views.PostDeleteView.as_view(),name="delete_post"),

    






]