from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html') 

    def post(self, request):
        return HttpResponse("Logged in")
