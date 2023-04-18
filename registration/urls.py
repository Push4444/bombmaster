"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from bomb import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login,name='Login'),
    path('Register/',views.Registration,name='Registration'),
    path('Escape/',views.Escape1,name='Escape'),
    path('End/',views.End,name='End'),
    path('Clue1/',views.Clue1,name='Clue1'),
    path('Clue2/',views.Clue2,name='Clue2'),
    path('Clue3/',views.Clue3,name='Clue3'),
    path('Clue4/',views.Clue4,name='Clue4'),
    path('Clue5/',views.Clue5,name='Clue5'),
    path('Clue6/',views.Clue6,name='Clue6'),
    path('Dead/',views.Dead,name='Dead'),
]
