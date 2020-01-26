from django.shortcuts import render
from django.http import HttpResponse
from .models import Lector, Course, Lesson
from django.shortcuts import render, get_object_or_404

def index_view(request):
    courses = Course.objects.all()
    return render(request, 'learnlearn/index.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'learnlearn/course_detail.html', {'course': course, 'lessons': lessons})
