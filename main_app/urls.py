from django.urls import path
from main_app.views import LoginView

urlpatterns = [
    path('', LoginView.as_view()),
]
