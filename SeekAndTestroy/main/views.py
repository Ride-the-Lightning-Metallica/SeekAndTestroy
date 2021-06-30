from django.shortcuts import render
from django.views.generic import DetailView, ListView

from main.models import Test, Category

def add_in_context(context):
    categories = Category.objects.all()
    context['categories'] = categories

    return context

class TestListView(ListView):
    model = Test
    template_name = "main/main.html"
    context_object_name = 'tests'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = add_in_context(super().get_context_data(**kwargs))
        return context

class TestDetailView(DetailView):
    model = Test
    template_name = "main/test_detail.html"

    def get_context_data(self, **kwargs):
        context = add_in_context(super().get_context_data(**kwargs))
        return context

class TestListByCategory(ListView):
    model = Test
    template_name = "main/main.html"
    context_object_name = 'tests'

    def get_queryset(self):
        return Test.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = add_in_context(super().get_context_data(**kwargs))
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        context['is_category_page'] = True
        return context


def about(request):
    return render(request, r'main\about.html', {})

def profile(request):
    return render(request, r'main\profile.html', {})

def archive(request):
    return render(request, r'main\archive.html', {})


