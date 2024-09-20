from django.urls import path
from school.views.school_view import  add_school, index_school, update_school,delete_school, checkschool, configurations
from school.views.app_settings_view import  add_setting, list_setting, check_settings,delete_setting,update_setting

app_name='school'

urlpatterns = [
    #CRUD school
    path('index_school',index_school,name="index_school"),
    path('school',add_school,name="add_school"),
    path('update_school/<int:id>',update_school,name="update_school"),
    path('checkschool/', checkschool, name='checkschool'),
    path('delete_school/<int:id>/', delete_school, name='delete_school'),
    
    #CRUD appSetting
    path('setting/',add_setting,name="add_setting"),
    path('list_setting/',list_setting,name="list_setting"),
    path('', check_settings, name='check_settings'),
    path('delete_setting/<int:id>/', delete_setting, name='delete_setting'),
    path('update_setting/<int:id>/', update_setting, name='update_setting'),
    
    path('configurations/', configurations, name="configurations"),
   
]
