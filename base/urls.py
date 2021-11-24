from django.contrib import admin
from django.urls import path, include

from .views import home, posts, post, sendEmail

urlpatterns = [
    path('', home, name="home"),
    path('projects/', posts, name="posts"),
    path('post/<slug:post_slug>/', post, name="post"),
    path('send_email/', sendEmail, name="send_email"),
]


