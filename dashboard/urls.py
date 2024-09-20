from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import index  # Renommer 'login' à 'custom_login' pour éviter les conflits
from .views import custom_logout,check_login,custom_login

app_name = 'dashboard'

urlpatterns = [
    path('home/', index, name='index'),
    # Utiliser LoginView de Django ou la vue custom, mais pas les deux
    path('', LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    # path('custom_login/', custom_login, name="custom_login"),
    path('logout/', custom_logout, name='logout'),
    path('checklogin/', check_login, name='check_login'),
]
    