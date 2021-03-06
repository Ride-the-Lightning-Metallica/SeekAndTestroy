from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.db.models import Q


from .models import Test, Category, User
from .forms import UserRegistrationForm


class TestListView(ListView):
    model = Test
    template_name = 'main/main.html'
    context_object_name = 'tests'
    paginate_by = 3

    def post(self, request):
        key = request.POST.get('key')
        fields_names = [
            'title', 'image', 'author__username',
            'category__title', 'description', 'difficulty'
        ]
        tests = self.get_queryset().values(*fields_names)
        tests = tests.filter(
            Q(title__icontains=key) |
            Q(author__username__icontains=key) |
            Q(description__icontains=key)
        )

        return JsonResponse({'tests': list(tests)}, safe=False)


class TestDetailView(DetailView):
    model = Test
    template_name = "main/test_detail.html"


class TestListByCategory(ListView):
    model = Test
    template_name = 'main/main.html'
    context_object_name = 'tests'

    def get_queryset(self):
        return Test.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        context['is_category_page'] = True
        return context


def about(request):
    return render(request, r'main\about.html')


@login_required
def profile(request):
    return render(request, r'main\profile.html')


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

    def form_valid(self, form):
        valid = super(UserRegistration, self).form_valid(form)
        username, password = (
            form.cleaned_data.get('username'),
            form.cleaned_data.get('password')
        )
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)

        return valid


class UserUpdateView(UpdateView):
    model = User
    fields = ('username', 'email', 'age', 'image', 'gender', 'country')
    template_name = 'main/profile_update.html'
    success_url = reverse_lazy('profile')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'main/confirm_delete.html'
    success_url = reverse_lazy('main')


class UserChangePasswordView(PasswordChangeView):
    template_name = 'main/change_password.html'
    success_url = reverse_lazy('profile')


class ArchiveListView(ListView):
    model = Test
    template_name = r'main\archive.html'
    context_object_name = 'tests'
    paginate_by = 3
