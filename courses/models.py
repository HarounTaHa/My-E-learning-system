from django.db import models

# Create your models here.

class Course(models.Model):
    SemesterNumber =(
        (1,1),
        (2,2),
    )
    name = models.CharField(max_length=200)
    semesterNumber = models.SmallIntegerField(choices=SemesterNumber)

    def __str__(self):
        return  f"{self.name} / الفصل : {str(self.semesterNumber)} "