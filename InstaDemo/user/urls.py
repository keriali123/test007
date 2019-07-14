from django.urls import path
from . import views

urlpatterns=[
    # path("",views.HelloDjango.as_view())
    path("home/",views.PostListView.as_view(),name="home"),
    path("post/<int:pk>/",views.PostDetailView.as_view(),name="post_detail")
    






]