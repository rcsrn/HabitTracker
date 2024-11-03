"""
URL configuration for habit_tracker project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    
Add an import:  from my_app import views
Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    
Add an import:  from other_app.views import Home
Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    
Import the include() function: from django.urls import include, path
Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import CustomLoginView,home,register,CustomLogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    # path("login/", CustomLoginView, name="login"),
    path("", home, name="home"),
    path("registro/", register, name="register"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]