
from django.urls import path
from .views.student_view import index,add, update, delete 
from .views.absence_view import add_abs,list_abs, update_abs 
from .views.studentCards_view import add_card, list_card



app_name="student"
urlpatterns = [
    path('', index,name="index"),
    path('add',add,name="add"),
    path('add_abs',add_abs,name="add_abs"),
    path('list_abs',list_abs,name="list_abs"),
    path('update_abs',update_abs,name="updateabs"),
    path('add_card',add_card,name="add_card"),
    path('list_card',list_card,name="list_card"),
    path('update/<int:id>',update,name="update-student"),
    path('delete/<int:id>',delete,name="delete-student"),
]