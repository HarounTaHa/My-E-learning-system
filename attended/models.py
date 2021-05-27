from django.db import models
from quizes.models import Quiz
from students.models import Student
# Create your models here.
class Attended(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    grade = models.FloatField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural='Attendees'