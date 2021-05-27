from django.db import models
from sections.models import Section


# Create your models here.

class Student(models.Model):
    Gender = (
        ('male', 'Male'),
        ('female','Female'),
    )
    identity_number = models.CharField(max_length=200,blank=True)
    password = models.CharField(max_length=200,blank=True)
    name = models.CharField(max_length=200)
    # birth_of_date = models.DateField(help_text='Date of birth',blank=True)
    gender = models.CharField(choices=Gender,max_length=50)
    phone_number = models.CharField(max_length=200,help_text='should be start +970',blank=True)
    token_notification = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.name

class RegisterStudent(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)

    def __str__(self):
        return f"اسم الطالب : {self.student} - {self.section}"