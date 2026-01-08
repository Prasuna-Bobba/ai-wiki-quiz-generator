from django.shortcuts import render
from .models import Quiz

def home(request):
    return render(request, "home.html")

def history(request):
    quizzes = Quiz.objects.all()
    return render(request, "history.html", {"quizzes": quizzes})
