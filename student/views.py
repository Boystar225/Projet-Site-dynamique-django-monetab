from django.shortcuts import render,redirect
from .models import Students
from .forms import StudentsForm


# Create your views here.

def index(request):
    students = Students.objects.all()
    total = Students.objects.count()
    return render(request, "student/index.html",{'students':students, 'total':total})

def edit(request, pk):
    if request.method == "POST":
        student = Students.objects.get(id=pk)
        form =StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:index')
    else:
        student = Students.objects.get(id=pk)
        students = StudentsForm(instance=student)
        
        
        context = {'students':students}
        return render(request, "student/edit.html",context)

def add(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:index')  # Redirect to users list after successful form submission.
        else:
            forms = StudentsForm()
            context= {'form':forms}
            context= {'error': "Invalid field submitted",'form':forms}
            return render(request, "student/add.html",context)
    else:
        forms = StudentsForm()
        context= {'form':forms}
        return render(request, "student/add.html",context)
    
def delete(request, pk):
    teacher = Students.objects.get(id=pk)
    teacher.delete()    
    
    return redirect(request,'student:index')
    

