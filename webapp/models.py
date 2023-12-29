from django.db import models

# Create your models here.
class studentresult(models.Model):
    student_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=200)
    subject_marks =models.CharField(max_length=200)
    result_code = models.CharField(max_length=100)

