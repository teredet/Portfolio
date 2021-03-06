from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse

from .models import Post


def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]

    context = {'posts': posts}
    return render(request, 'base/home.html', context)


def posts(request):
    posts = Post.objects.filter(active=True)

    context = {'posts': posts}
    return render(request, 'base/posts.html', context)


def post(request,post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, f'base/posts/{post.slug}.html', {'post': post})

def profile(request):
    return render(request, 'base/profile.html')


def sendEmail(request):
    if request.method == 'POST':

        template = render_to_string('base/email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['artem.vanzytler@gmail.com']
        )

        email.fail_silently=False
        email.send()

    return HttpResponse('Email was sent!')
