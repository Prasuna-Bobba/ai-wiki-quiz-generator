from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Quiz

def home(request):
    quiz = None
    error = None

    if request.method == "POST":
        wiki_url = request.POST.get("wiki_url")

        if not wiki_url:
            error = "Please enter a Wikipedia URL."
        else:
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                }

                response = requests.get(wiki_url, headers=headers, timeout=15)

                #  CHECK RESPONSE
                if response.status_code != 200:
                    raise Exception("Wikipedia page not reachable")

                soup = BeautifulSoup(response.text, "html.parser")

                h1 = soup.find("h1")
                if not h1:
                    raise Exception("Title not found")

                title = h1.get_text(strip=True)

                # Save quiz
                Quiz.objects.create(
                    title=title,
                    url=wiki_url
                )

                quiz = {
                    "title": title,
                    "questions": [
                        {
                            "question": "What is this Wikipedia article mainly about?",
                            "options": [
                                "Science",
                                "Technology",
                                "History",
                                "All of the above"
                            ],
                            "answer": "All of the above",
                            "difficulty": "easy",
                            "explanation": "Based on the introductory section of the article."
                        }
                    ]
                }

            except Exception as e:
                error = f"Unable to fetch Wikipedia content: {str(e)}"

    return render(request, "home.html", {
        "quiz": quiz,
        "error": error
    })


def history(request):
    return render(request, "history.html")
