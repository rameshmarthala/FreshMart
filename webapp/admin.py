from django.contrib import admin
from .models import studentresult
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display = ['student_name','subject_code','subject_name','subject_marks','result_code']
admin.site.register(studentresult,studentadmin)