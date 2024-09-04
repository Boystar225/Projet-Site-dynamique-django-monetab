from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from student.models import Students
from teacher.models import Teacher
from django.contrib.auth.models import User

@login_required
def index(request):
    totalstudent = Students.objects.count()
    totalteacher =  Teacher.objects.count()
    totaluser = User.objects.count()
    return render(request, "dashboard/index.html", {'totalstudent':totalstudent, 'totalteacher':totalteacher, 'totaluser':totaluser})

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard:home')
        else:
            return render(request, "dashboard/login.html", {"error": "Identifiant ou mot de passe incorrect."})

    return render(request, "dashboard/login.html")

def custom_logout(request):
    logout(request)
    return redirect('dashboard:login')  # Redirige vers la page de connexion