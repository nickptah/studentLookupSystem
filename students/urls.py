from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('dashboard/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/students/add/', views.student_create, name='student_add'),
    path('dashboard/students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('dashboard/students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('dashboard/import/', views.import_excel, name='import_excel'),
]
