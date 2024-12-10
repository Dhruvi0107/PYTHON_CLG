from django.contrib import admin
from django.urls import path
from First_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',views.registration,name="student_registration")
]