from django.contrib import admin
from django.urls import path
from Que1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home_Page"),
    path('add_student/',views.addStudent,name="Add_Student"),
    path('list_student/',views.listStudent,name="List_Student"),
    path('filter_student/',views.filterStudent,name="Filter_Student"),
    path('delete_student/',views.deleteStudent,name="Delete_Student"),
    path('update_student/<int:student_ID>/',views.updateStudent,name="Update_Student"),
]