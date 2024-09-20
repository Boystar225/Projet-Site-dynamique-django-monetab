from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from school.forms.school_form import SchoolForms
from school.models.school_model import SchoolModel


@login_required
def index_school(request):
    schools = SchoolModel.objects.all()
    school_count = SchoolModel.objects.count()
    context = {
        'schools':schools,
        'school_count':school_count
        
    }
    return render(request, "school/list_school.html", context)

def add_school(request):
    context={"title":"Ajouter une école"}

    if request.method == "POST":
        print(request.POST)
        form2 =SchoolForms(request.POST)
        context["form2"] = form2
        if form2.is_valid():
            print("form is valid")
            print(form2.cleaned_data)
            form2.save()
            return redirect('dashboard:login')
        else:
            return render(request,"school/school.html")

    # context={'elev_form':elev_form}
    form2 = SchoolForms()
    context["form2"] = form2

    return render(request,"school/school.html",context)

@login_required
def update_school(request, id):
    # user = get_object_or_404(User,id = id)
    school = SchoolModel.objects.get(id=id)
 
    context = {
        "title":"Modifier l'école"
    }

    if request.method == "POST":
        form2 = SchoolForms(request.POST, instance=school)
        if form2.is_valid():
            form2.save()
            return redirect('school:index_school')
        
    form2 = SchoolForms(instance = school)

    context["form"] = form2

    return render(request,"school/school.html",context)


def checkschool(request):
    school = SchoolModel.objects.first()
    
    if not school: #if there is no school
        return redirect('school:add_school') #to add a school
    else:
        return redirect('dashboard:check_login') #to check the role


@login_required
def delete_school(request,id):
    school = get_object_or_404(SchoolModel, id=id)
    school.delete()
    return redirect('school:list_school')


@login_required
def configurations(request):
    return render(request, "school/settings.html")