from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('archive/', views.archive, name='archive'),
    path('test/<slug:slug>', views.TestDetailView.as_view(), name='test_detail')
]