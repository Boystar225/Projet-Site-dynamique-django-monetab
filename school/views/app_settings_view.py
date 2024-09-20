from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from school.forms.appSetting_form import AppSettingForms
from school.models.app_settings_model import AppSettingModel

@login_required
def list_setting(request):
    aps = AppSettingModel.objects.all()
    ap_count = AppSettingModel.objects.count()
    context = {
        'aps':aps,
        'ap_count':ap_count
        
    }
    return render(request, "school/list_app.html", context)


def add_setting(request):
    context = {"title": "Ajout AppSetting"}

    if request.method == "POST":
        form3 = AppSettingForms(request.POST)
        context["form3"] = form3
        if form3.is_valid():
            form3.save()
            return redirect('school:add_school')
        else:
            # Affiche le formulaire avec les erreurs s'il n'est pas valide
            return render(request, "school/appSettings.html", context)

    # Si la méthode n'est pas POST, initialisez un formulaire vide
    form3 = AppSettingForms()
    context["form3"] = form3

    # Récupérer tous les paramètres de configuration de l'application
    app_setting = AppSettingModel.objects.all()
    if not app_setting:
        # Si aucun paramètre trouvé, affiche le formulaire
        return render(request, "school/appSettings.html", context)
    else:
        # Redirige vers l'ajout d'école si un paramètre existe déjà
        return redirect('school:add_school')

@login_required
def update_setting(request,id):
    setting = get_object_or_404(AppSettingModel, id=id)
    if request.method== 'POST':
        form = AppSettingForms(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            return redirect('school:index_school')
    else:
        form = AppSettingForms(instance=setting)
    return render(request, 'school/edit.html')
    
@login_required
def delete_setting(request,id):
    setting = get_object_or_404(AppSettingModel,id=id)
    setting.delete()
    return redirect('school:list_setting')
    

def check_settings(request):
    app_setting = AppSettingModel.objects.first()
    
    print(app_setting)
    
    if not app_setting:
        return redirect('school:add_setting') #pour ajouter parametre 
    
    else:
        return redirect('school:checkschool') #pour verifier l'ecole
    



