"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from django.contrib.auth import views as auth_views  # for login/logout
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.task_list, name='task_list'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
     path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),  # ✅ new
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),  # ✅ new route
     # ✅ Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register_user, name='register'),
    path('export/', views.export_tasks_csv, name='export_tasks_csv'),
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('calendar-data/', views.get_tasks_json, name='calendar_data'),  # 🆕
    # other paths...
]
