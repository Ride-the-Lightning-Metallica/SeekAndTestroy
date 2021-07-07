from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from .models import Test, Category, User
from .forms import UserRegistrationForm

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
    return render(request, r'main\about.html')

@login_required
def profile(request):
    context = add_in_context({})
    return render(request, r'main\profile.html', context)

class UserLoginView(LoginView):
    template_name = 'main/login.html'
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    next_page = 'main'

class UserRegistration(CreateView):
    model = User
    template_name = 'main/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
class UserDeleteView(DeleteView):
    model = User
    template_name = 'main/confirm_delete.html'
    success_url = reverse_lazy('main')
    

def archive(request):
    return render(request, r'main\archive.html', {})


