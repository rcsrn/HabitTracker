"""
URL configuration for habit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from users.views import CustomLoginView,home,registro,logout_view,habito, estadistica, comunidad, config

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    # path("login/", CustomLoginView, name="login"),
    path("", home, name="home"),
    path("registro/", registro.as_view(), name="registro"),

    path("logout/", logout_view, name="logout"),
    path("habito/", habito, name="habito"),
    path("estadisticas/", estadistica, name="estadisticas"),
    path("comunidad/", comunidad, name="comunidad"),
    path("config/", config, name="config"),
    
    
]
