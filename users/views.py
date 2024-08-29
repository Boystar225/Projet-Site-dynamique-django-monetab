from django.shortcuts import redirect, render

from .forms import UserForm

from .models import User


# Create your views here.

def index(request):
    user = User.objects.all()
    return render(request, "users/index.html",{'users':user})

def edit(request, pk):
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:index')
    else:
        user = User.objects.get(id=pk)
        form = UserForm(instance=user)
        
        
        context = {'form':form}
        return render(request, "users/edit.html",context)

def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:index')  # Redirect to users list after successful form submission.
    else:
        forms = UserForm()
        context= {'form':forms}
        return render(request, "users/add.html",context)
    

