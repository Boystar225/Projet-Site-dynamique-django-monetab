from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models.user_model import CustomUserModel
from user.forms.user_form import UserFoms

@login_required
def index(request):
    search_field = request.GET.get('search')
    if search_field :
        users = CustomUserModel.objects.filter(pseudo__icontains=search_field)
        context = {
            'users': users,
            'search_field': search_field,
        }
    else:
        users = CustomUserModel.objects.all()
        user_count = CustomUserModel.objects.count()
        context = {
            'users':users,
            'user_count':user_count
        
    }
    return render(request, "user/index.html", context)

@login_required
def add(request):
    context={"title":"Ajouter Utilisateur"}

    if request.method == "POST":
        print(request.POST)
        form =UserFoms(request.POST)
        context["form"] = form
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect('user:index')
        else:
            return render(request,"user/add.html")

    form = UserFoms()
    context["form"] = form

    return render(request,"user/add.html",context)

@login_required
def update(request, id):
    user = CustomUserModel.objects.get(id=id)
 
    context = {
        "title":"Modifier utilisateur"
    }

    if request.method == "POST":
        form = UserFoms(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:index')
        
    form = UserFoms(instance = user)

    context["form"] = form

    return render(request,"user/add.html",context)

