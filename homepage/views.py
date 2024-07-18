from django.http import HttpResponse
from django.shortcuts import render
import django.template
from django.template.loader import get_template
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def index(request):
    print(dir_path)
    get_template("index.html")
    return render(request, "index.html")
