import random
from urllib.parse import urlparse

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login as auth_login
from django.urls import is_valid_path

from .models import *
from .forms import ReviewForm, RegistrationForm, LoginForm


def index(request):
    try:
        books = random.sample(list(Book.objects.all()), 3)
    except ValueError:
        books = None
    return render(request, 'index.html', {'books': books})


def view_author(request, author_id):
    author = Author.objects.get(id=author_id)
    print(request.user)
    return render(request, 'author.html', {'author': author})


def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        user = request.user
        if form.is_valid():
            review = Review(content=form.cleaned_data['content'], author=user, book=book)
            review.save()
            return redirect(request.path)
    else:
        form = ReviewForm()
    return render(request, 'book.html', {'book': book, 'form': form})


def login_user(request):
    next_url = request.GET.get('next', '/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=username, password=password)
            auth_login(request, user)
            next_url = request.POST.get('next', next_url)
            parsed_url = urlparse(next_url)
            if not parsed_url.netloc and is_valid_path(next_url):
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'next': next_url})


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required
def view_user(request):
    pass