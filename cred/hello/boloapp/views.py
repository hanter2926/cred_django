from django.shortcuts import render
from .models import Student

# READ (Show all students)
def index(request):
    data = Student.objects.all()
    return render(request, 'index.html', {'data': data})
