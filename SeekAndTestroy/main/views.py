from typing import List
from django.shortcuts import render

from main.models import Test

def main(request):
    tests = Test.objects.all()
    return render(request, r'main\main.html', {'tests': tests})

def about(request):
    return render(request, r'main\about.html', {})

def profile(request):
    return render(request, r'main\profile.html', {})

def archive(request):
    return render(request, r'main\archive.html', {})