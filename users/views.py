from django.shortcuts import redirect, render
from .forms import UserForm
from django.contrib.auth.models import User # Import the User model from django.contrib.auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from .models import Use

@login_required
def index(request):
    user = User.objects.all()
    total = User.objects.count()
    return render(request, "users/index.html",{'users':user,'total':total})
@login_required
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

@login_required
def add(request):
    context = {"title": "Add User"}

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # Vérifier si les champs sont remplis
        if not username or not password:
            messages.error(request, "Le nom d'utilisateur et le mot de passe sont obligatoires.")
            return render(request, "users/add.html", context)

        # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà.")
            return render(request, "users/add.html", context)

        # Créer un utilisateur avec le mot de passe haché
        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Utilisateur créé avec succès.")
        return redirect('users:index')  # Redirige vers l'URL appropriée après l'ajout de l'utilisateur

    return render(request, "users/add.html", context)

@login_required
def delete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('users:index')


