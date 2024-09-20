from django.urls import path
from .views import add_adresse


app_name="adress"
urlpatterns = [
    path('add_adresse',add_adresse,name="add_adresse"),
    # path('update/<int:id>',update,name="update-student"),
    # path('delete/<int:id>',delete,name="delete-student"),
]