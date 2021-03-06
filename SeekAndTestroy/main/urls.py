from django.urls import path

from . import views

urlpatterns = [
    path('', views.TestListView.as_view(), name='main'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path(
        'profile/update/<slug:slug>/',
        views.UserUpdateView.as_view(),
        name='profile_update'
    ),
    path(
        'profile/change/password/',
        views.UserChangePasswordView.as_view(),
        name='change_password'
    ),
    path(
        'profile/delete/<slug:slug>/',
        views.UserDeleteView.as_view(),
        name='delete_profile'
    ),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('registration/', views.UserRegistration.as_view(), name='registration'),
    path('archive/', views.ArchiveListView.as_view(), name='archive'),
    path('test/<slug:slug>/', views.TestDetailView.as_view(), name='test_detail'),
    path('category/<slug:slug>/',
         views.TestListByCategory.as_view(), name='by_category')
]
