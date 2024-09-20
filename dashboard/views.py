from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from student.models.student_model import StudentModel
from teacher.models.teacher_model import TeacherModel
from django.contrib.auth.models import User
from school.models.app_settings_model import AppSettingModel
from school.models.school_model import SchoolModel

@login_required
def index(request):
    totalstudent = StudentModel.objects.count()
    totalteacher =  TeacherModel.objects.count()
    totaluser = User.objects.count()
    return render(request, "dashboard/index.html", {'totalstudent':totalstudent, 'totalteacher':totalteacher, 'totaluser':totaluser})

def custom_login(request):
    count_app_setting = AppSettingModel.objects.count()
    count_school = SchoolModel.objects.count()
    if count_app_setting ==1:
        if count_school == 1:
            #Vérifier si l'utilisateur est déjà connecté 
            if request.user.is_authenticated:
                return redirect('dashboard:index')
            #Traitement du formulaire de connexion 
            if request.method == "POST":
                username = request.POST.get("username")
                password = request.POST.get("password")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('dashboard:index')
                else:
                    return render(request, "dashboard/login.html", {"error": "Identifiant ou mot de passe incorrect."})
            else:
                return redirect('school:checkschool')
        else:
            return redirect('school:check_settings')
            # return render(request, "dashboard/login.html")
        
@login_required
def custom_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('dashboard:login')  # Redirige vers la page de connexion
    return redirect('dashboard:login') 
    

def check_login(request):
    count_app_setting = AppSettingModel.objects.count()
    count_school = SchoolModel.objects.count()
    if count_app_setting ==1:
        if count_school == 1:
            #Vérifier si l'utilisateur est déjà connecté 
            if request.user.is_authenticated:
                return redirect('dashboard:index')
            else:
                return redirect('dashboard:login')
        else:
            return redirect('school:checkschool')
    else:
        return redirect('school:check_settings')