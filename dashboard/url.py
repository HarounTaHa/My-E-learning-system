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
    path('teacher/edit/<pk>/', teacher_edit, name='dashboard_teacher_edit'),
    path('teacher/delete/<pk>/', teacher_delete, name='dashboard_teacher_delete'),

    path('course/', course_show, name='dashboard_course_show'),
    path('course/add', course_add, name='dashboard_course_add'),
    path('course/edit', course_edit, name='dashboard_course_edit'),


    path('quiz/', quiz_show, name='dashboard_quiz_show'),
    path('quiz/<pk>/', quiz_view, name='dashboard_quiz_view'),
    path('quiz/<pk>/save/', save_quiz_view, name='dashboard_save_quiz_view'),
    path('quiz/<pk>/data/', quiz_data_view, name='dashboard_quiz_data_view'),
    path('quiz/add', quiz_add, name='dashboard_quiz_add'),
    path('quiz/edit', quiz_edit, name='dashboard_quiz_edit'),


]