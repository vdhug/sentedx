from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
	return render(request, "personal/index.html")


def contact(request):
	return render(request, "personal/basic.html", {"content": ["Hi", "vitor@gmail.com"]})