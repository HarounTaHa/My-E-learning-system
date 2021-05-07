from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# Create your views here.
# ------Authentication------------
def login_page(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            username = User.objects.get(email=email).username
        except:
            username=email
        auth= authenticate(request,username=username,password=password)
        if auth:
            login(request,auth)
            return redirect('dashboard_home')
        else:
            print('Try Again')
    return render(request,'authentication/login.html')

def register_page(request):
    return HttpResponse('Test')


def homePage(request):
    # data = {
    #     'count_students':Student.objects.all().count(),
    #     'count_teachers':Teacher.objects.all().count(),
    #     'count_sections':Section.objects.all().count(),
    # }
    return render(request,'dashboard_home.html')

# -----------------Section------------------------------------
def section_show(request):
    return render(request,'sections/show_section.html')

def section_edit(request):
    return render(request,'sections/edit_section.html')


def section_add(request):
    # if request.method=='POST':
    # name_section=request.POST['name_section']
    #     .....
    #     .....
    #     .....
    #     .....
    #     .....
    return render(request,'sections/add_section.html')

# -----------------Student------------------------------
def student_show(request):
    return render(request,'students/show_student.html')

def student_edit(request):
    return render(request,'students/edit_student.html')


def student_add(request):
    # if request.method=='POST':
    # name_student=request.POST['name_student']
    #     .....
    #     .....
    #     .....
    #     .....
    #     .....
    return render(request,'students/add_student.html')

# -------------Teacher----------------------------------------
def teacher_show(request):

    return render(request,'teachers/show_teacher.html')

def teacher_edit(request):
    return render(request,'teachers/edit_teacher.html')


def teacher_add(request):
    # if request.method=='POST':
    # name_teacher=request.POST['name_teacher']
    #     .....
    #     .....
    #     .....
    #     .....
    # by_user=request.user.id

    return render(request,'teachers/add_teacher.html')

# -----------------Course------------------------------------
def course_show(request):
    return render(request,'courses/show_course.html')

def course_edit(request):
    return render(request,'courses/edit_course.html')


def course_add(request):
    # if request.method=='POST':
    # name_section=request.POST['name_section']
    #     .....
    #     .....
    #     .....
    #     .....
    #     .....
    return render(request,'courses/add_course.html')