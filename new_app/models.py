from django.db import models

# Create your models here.

class StudentData(models.Model):
    name = models.CharField(max_length=300)
    student_id = models.CharField(max_length=20)
    add = models.CharField(max_length=500)
    class Meta:
        verbose_name_plural ='Student Datas'

    def __str__(self):
        return self.name

