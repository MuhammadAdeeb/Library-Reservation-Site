"""rev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from pages.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    # path('', include("main.urls")), # Not sure if this is correct/needed; from a diff youtube vid I think
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include("django.contrib.auth.urls")),  # Go to this application for valid URLs
        # Don't exit yet; login.html, login.html and we need to create a folder for them  to allow retrieval
    # path('accounts/', include('django.contrib.auth.urls')),
]
