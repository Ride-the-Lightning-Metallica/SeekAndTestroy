from django.urls import path

from . import views

urlpatterns = [
    path('', views.TestListView.as_view(), name='main'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('archive/', views.archive, name='archive'),
    path('test/<slug:slug>', views.TestDetailView.as_view(), name='test_detail'),
    path('category/<slug:slug>/', views.TestListByCategory.as_view(), name='by_category')
]