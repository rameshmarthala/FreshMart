from django.shortcuts import render
from webapp.models import studentresult
# Create your views here.
def studentview(request):
    result = studentresult.objects.filter(subject_marks__gte=30)
    return render(request, 'myapp/orm.html',{'result':result})