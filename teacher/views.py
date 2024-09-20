from django.shortcuts import render,redirect
from teacher.models.teacher_model import TeacherModel
from .forms import TeacherForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    search_field = request.GET.get('search')
    if search_field :
        # Filtrer les étudiants par nom ou prénom selon le terme de recherche
            teachers = TeacherModel.objects.filter(
            last_name__icontains=search_field
            ) | TeacherModel.objects.filter(
            first_name__icontains=search_field
            )
            context = {
            'teachers': teachers,
            'search_field': search_field,
        }

    else:
        teachers = TeacherModel.objects.all()
        student_count = TeacherModel.objects.count()
        context = {
            'teachers':teachers,
            'teacher_count': student_count,
            
    }
    teachers = TeacherModel.objects.all()
    total = TeacherModel.objects.count()
    return render(request, "teacher/index.html",{'teachers':teachers,'total':total})

@login_required
def edit(request, pk):
    if request.method == "POST":
        teacher = TeacherModel.objects.get(id=pk)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher:index')
    else:
        teacher = TeacherModel.objects.get(id=pk)
        teachers = TeacherForm(instance=teacher)
        
        
        context = {'teachers':teachers}
        return render(request, "teacher/edit.html",context)


@login_required
def add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher:index')  # Redirect to users list after successful form submission.
        else:
            forms = TeacherForm()
            context= {'form':forms}
            context= {'error': "Invalid field submitted",'form':forms}
            return render(request, "teacher/add.html",context)
    else:
        forms = TeacherForm()
        context= {'form':forms}
        return render(request, "teacher/add.html",context)
@login_required  
def delete(request, pk):
    teacher = TeacherModel.objects.get(id=pk)
    teacher.delete()
    return redirect('teacher:index')
    

