from django.shortcuts import render
from django.http import HttpResponse
from .models import course,lesson
# Create your views here.
def courses(request) :
    courses = course.objects.all()
    return render(request , 'courses.html' ,{'courses' : courses})