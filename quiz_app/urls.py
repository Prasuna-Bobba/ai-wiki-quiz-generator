from django.urls import path
from .views import home, history

urlpatterns = [
    path('', home),
    path('history/', history),
]
