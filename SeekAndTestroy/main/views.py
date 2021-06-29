from django.shortcuts import render
from django.views.generic import DetailView

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

class TestDetailView(DetailView):
    model = Test
    template_name = "main/test_detail.html"
