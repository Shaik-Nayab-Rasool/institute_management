from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page),
    path("dash/",views.admin_dashboard, name='dash'),
    path('create_student/',views.create_student,name='create_student'),
    path('update_student/<int:input_id>',views.update_student, name='update_student'),
    path('delete_student/<int:input_id>',views.delete_student,name='delete_student'),
    path('create_course/',views.create_course,name='create_course'),
    path('add_course_student/',views.add_course_student,name='add_course_student')
]