from django.urls import path,include,re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from rest_framework import permissions

from .viewsets.absence_viewset import AbsenceViewSet
from .viewsets.student_viewset import StudentViewset
from .viewsets.teacher_viewset import TeacherViewset
from .viewsets.user_viewset import CustomUserViewset
from .viewsets.app_setting_viewset import AppsettingViewSet
from .viewsets.school_viewset import SchoolViewSet
from .viewsets.role_user_viewset import RoleUserViewSet
from .viewsets.adresse_viewset import AdresseViewSet

app_name='api'

#Avec la methode de drf-yasg 
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

#Avec la nouvelle methode routers de rest_framework
routers = routers.DefaultRouter()
routers.register(r'students', StudentViewset, basename='students'),
routers.register(r'teachers', TeacherViewset, basename='teachers'),
routers.register(r'users', CustomUserViewset, basename='users'),
routers.register(r'schools',SchoolViewSet , basename='schools'),
routers.register(r'app-setting', AppsettingViewSet, basename='appsetting'),
routers.register(r'role-user', RoleUserViewSet, basename='roleuser'),
routers.register(r'address', AdresseViewSet, basename='adresse'),
routers.register(r'absence', AbsenceViewSet, basename='absence'),





urlpatterns = [
    path('', include(routers.urls)),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
]























# from django.urls import path, include
# from rest_framework import routers
# from .api_view.student_view import Student_list,student_detail
# from .api_view.teacher_view import Teacher_list, teacher_detail
# from .api_view.user_view import User_list, user_detail

# #Avec la nouvelle methode 

# routers = routers.DefaultRouter()
# routers.register(r'students', StudentViewset)
# app_name = 'api'
# urlpatterns = [
#     #Students routes
#     path('students/', Student_list),
#     path('students/<int:pk>/', student_detail),
    
#     #Teachers routes
    
#     path('teachers/', Teacher_list),
#     path('teachers/<int:pk>/', teacher_detail),
    
#     #Users routes 
    
#     path('users/', User_list),
#     path('users/<int:pk>/', user_detail),
    
# ]
