from django.db import models

# Create your models here.
class Section(models.Model):

    level = models.SmallIntegerField(verbose_name='صف')
    branch = models.SmallIntegerField(verbose_name='فرع')

    def __str__(self):
        return  f" الصف : {str(self.level)}/{str(self.branch)}"