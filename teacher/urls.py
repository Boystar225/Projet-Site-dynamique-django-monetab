from django.urls import path
from .views import index
from .views import add
from .views import edit,delete

app_name = 'teacher'
urlpatterns = [
    
    path('', index, name='index'),
    path('add', add, name='add'),
    path('edit/<str:pk>/', edit, name='edit'),
    path('delete/<str:pk>/', delete, name='delete'),
    
]
