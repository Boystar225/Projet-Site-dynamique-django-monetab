from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.forms.roleUser_form import RoleUserFoms
from user.models.roleUser_model import RoleUserModel
@login_required
def index_role(request):
    roles = RoleUserModel.objects.all()
    role_count = RoleUserModel.objects.count()
    context = {
        'roles':roles,
        'role_count':role_count
        
    }
    return render(request, "user/list_role.html", context)

@login_required
def role(request):

    context={"title":"Ajout Role"}

    if request.method == "POST":
        print(request.POST)
        form1 =RoleUserFoms(request.POST)
        context["form1"] = form1
        if form1.is_valid():
            print("form is valid")
            print(form1.cleaned_data)
            form1.save()
            return redirect('user:index_role')
        else:
            return render(request,"user/roleUser.html")

    # context={'elev_form':elev_form}
    form1 = RoleUserFoms()
    context["form1"] = form1

    return render(request,"user/roleUser.html",context)
