from django.db import models
from courses.models import Course
from sections.models import Section

# Create your models here.

class Teacher(models.Model):
    Gender = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    identityNumber = models.CharField(max_length=60,blank=True)
    password=models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(choices=Gender,max_length=50)
    phoneNumber = models.IntegerField(help_text="phone number for teacher should be start +970",null=True,blank=True)
    tokenNotification = models.CharField(max_length=300,help_text='use for notification cloud',null=True,blank=True)

    def __str__(self):
        return self.name


class Teaches (models.Model):
    teacher = models.ForeignKey(Teacher,on_delete = models.CASCADE)
    course = models.ForeignKey(Course,on_delete= models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    def __str__(self):
        return f" اسم المدرس  : {str(self.teacher.name)} - المادة : {str(self.course.name)} - الصف : {str(self.section.level)} " \
               f"/{str(self.section.branch)}"


