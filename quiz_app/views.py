import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Quiz, Question

def home(request):
    quiz = None

    if request.method == "POST":
        url = request.POST.get("url")

        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("h1").text

        quiz = Quiz.objects.create(url=url, title=title)

        # Sample questions (guaranteed to show)
        Question.objects.create(
            quiz=quiz,
            question="What is Artificial Intelligence?",
            option_a="A branch of biology",
            option_b="Simulation of human intelligence in machines",
            option_c="A hardware device",
            option_d="A programming language",
            answer="B",
            explanation="AI simulates human intelligence in machines."
        )

        Question.objects.create(
            quiz=quiz,
            question="Which field is related to AI?",
            option_a="Machine Learning",
            option_b="Civil Engineering",
            option_c="Mechanical Design",
            option_d="Accounting",
            answer="A",
            explanation="Machine Learning is a core part of AI."
        )

    return render(request, "home.html", {"quiz": quiz})


def history(request):
    quizzes = Quiz.objects.all()
    return render(request, "history.html", {"quizzes": quizzes})

