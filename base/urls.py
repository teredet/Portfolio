from django.contrib import admin
from django.urls import path, include

from .views import home, posts, profile, sendEmail

urlpatterns = [
    path('', home, name="home"),
    path('posts/', posts, name="posts"),

    path('send_email/', sendEmail, name="send_email"),
]


