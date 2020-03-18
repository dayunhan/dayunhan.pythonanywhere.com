from . import views

from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
]
