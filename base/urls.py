from django.contrib import admin
from django.urls import path, include

from .views import home, posts, post, profile, sendEmail

urlpatterns = [
    path('', home, name="home"),
    path('posts/', posts, name="posts"),
    path('post-details/', post, name="post_details"),
    path('send_email/', sendEmail, name="send_email"),
]


