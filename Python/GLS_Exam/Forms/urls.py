from django.contrib import admin
from django.urls import path
from Forms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.addMobile,name="mobile_add"),
    path('thanks/',views.thannks,name="Thank_you"),
]