from django.shortcuts import render
from .models import Student
def index(request):
    get_all_students = Student.objects.all()
    context = {
        'students':get_all_students
    }
    return render(request, 'index.html', context)