from django.shortcuts import render, redirect
from .forms import AdressFoms
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AdressFoms
@login_required
# Create your views here.
def add_adresse(request):
    if request.method == "POST":
        form = AdressFoms(request.POST)
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect('student:index')
        else:
            context = {
                "title": "Ajouter une adresse",
                "form": form
            }
            return render(request, "base/adress.html", context)
    else:
        form = AdressFoms()
        context = {
            "title": "Ajouter une adresse",
            "form": form
        }
        return render(request, "base/adress.html", context)
