from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(homePage),name='dashboard_home'),
    path('section/',section_show,name='dashboard_section_show'),
    path('section/add',section_add,name='dashboard_section_add'),
    path('section/edit',section_edit,name='dashboard_section_edit'),

    path('student/', student_show, name='dashboard_student_show'),
    path('student/add', student_add, name='dashboard_student_add'),
    path('student/edit', student_edit, name='dashboard_student_edit'),

    path('teacher/', teacher_show, name='dashboard_teacher_show'),
    path('teacher/add', teacher_add, name='dashboard_teacher_add'),
    path('teacher/edit', teacher_edit, name='dashboard_teacher_edit'),

    path('course/', course_show, name='dashboard_course_show'),
    path('course/add', course_add, name='dashboard_course_add'),
    path('course/edit', course_edit, name='dashboard_course_edit'),


]