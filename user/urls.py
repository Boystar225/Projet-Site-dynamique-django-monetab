from django.urls import path
from user.views.user_view import index,add,update
from .views.roleUser_view import role, index_role 



app_name = 'user'
urlpatterns = [
    
    path('', index, name='index'),
    path('add', add, name='add'),
    path('edit/<str:pk>/', update, name='edit'),
    
    
    #CRUD role
    path('role',role,name="role"),
    path('index_role',index_role,name="index_role"),
    
    
]

