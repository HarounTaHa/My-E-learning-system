from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from quizes.models import Quiz
from teachers.models import Teaches,Teacher
from questions.models import Question,Answer
from courses.models import Course
from students.models import Student
from sections.models import Section
from django.http import JsonResponse
from attended.models import Attended
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
    data = {
        'count_students':Student.objects.all().count(),
        'count_teachers':Teacher.objects.all().count(),
        'count_sections':Section.objects.all().count(),
        'count_quizzes':Quiz.objects.all().count(),
        'count_courses':Course.objects.all().count(),
    }
    return render(request,'dashboard_home.html',data)

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
    data = {
        'teachers': Teacher.objects.all(),
    }
    return render(request , 'teachers/show_teacher.html' , data)

def teacher_edit(request,pk):
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


def teacher_delete(request,pk):
    teacher = Teacher.objects.get(pk=pk)
    teacher.delete()
    return redirect('dashboard_teacher_show')

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

# ------------------Quiz---------------------------------
def quiz_show(request):
    quizes=Quiz.objects.all()
    return render(request,'quizes/show_quiz.html',{'objects':quizes})

def quiz_view(request,pk):
    quiz=Quiz.objects.get(pk=pk)
    return render(request,'quizes/quiz.html',{'obj':quiz})


def quiz_data_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q):answers})

    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

def save_quiz_view(request,pk):
    # print(request.POST)
    if request.is_ajax():
        grade = 0
        questions = []
        data=request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        for k in data_.keys():
            print("key : ",k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)
        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        results = []
        correct_answer = None
        for q in questions:
            answer_selected = request.POST.get(q.text)
            if answer_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if answer_selected == a.text:
                        if a.correct:
                            grade += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({str(q): {'correct answer':correct_answer,'answered': answer_selected}})
            else:
                results.append({str(q): 'not answered'})
        # Attended.objects.create(quiz=quiz,user=user,grade=grade)
        # بدل user يجب نضع student
        if grade >= 3 :
            return JsonResponse({'passed':True,'grade':grade,'results':results})
        else:
            return JsonResponse({'passed':False,'grade':grade,'results':results})


def quiz_edit(request):
    return render(request,'quizes/edit_quiz.html')


def quiz_add(request):
    # if request.method=='POST':
    # name_teacher=request.POST['name_teacher']
    #     .....
    #     .....
    #     .....
    #     .....
    # by_user=request.user.id

    return render(request,'quizes/add_quiz.html')