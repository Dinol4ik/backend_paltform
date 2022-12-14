from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError


def auth(request):
    users = User.objects.filter(username="asdsad")
    return render(request,'authentication/registration.html')

def reg(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = User.objects.create(
            username=name,
            email=email
        )
    except IntegrityError:
        return HttpResponse(400)
    user.set_password(password)
    user.save()
    login(request, user)
    return redirect('/')
