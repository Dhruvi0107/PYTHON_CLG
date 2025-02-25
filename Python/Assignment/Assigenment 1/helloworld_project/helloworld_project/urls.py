"""
URL configuration for helloworld_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from first_app import urls
from secound_app import urls
from third_app import urls
from four_app import urls
from fifth_app import urls
from six_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/',include('first_app.urls')),
    path('secound_app/',include('secound_app.urls')),
    path('third_app/',include('third_app.urls')),
    path('four_app/',include('four_app.urls')),
    path('fifth_app/',include('fifth_app.urls')),
    path('six_app/',include('six_app.urls')),
]
