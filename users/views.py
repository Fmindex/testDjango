from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the users index.")

def new(request):
	return HttpResponse("Hello, world. You're at the users new page.")