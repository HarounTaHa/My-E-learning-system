from django.db import models
from courses.models import Course
from teachers.models import Teacher
from sections.models import Section
from django.utils import timezone

import random
# Create your models here.
class Quiz(models.Model):
    quiz_name = models.CharField(max_length=120)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    number_of_question = models.IntegerField()
    is_available = models.BooleanField(default=False)
    quiz_date_created = models.DateTimeField('quiz_date_created', default=timezone.now, blank=False)
    # time_in = models.TimeField(null=True)
    # time_out = models.TimeField(null=True)
    time = models.IntegerField(help_text="duration of the quiz in minute")

    def __str__(self):
        return f"{self.quiz_name}- {self.course.name}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_question]

    class Meta:
        verbose_name_plural='Quizes'