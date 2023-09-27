from django.shortcuts import render
from .models import Malumot


# Create your views here.


def info(request):
    posts = Malumot.objects.all()
    return render(request, "site.html", {"posts": posts})