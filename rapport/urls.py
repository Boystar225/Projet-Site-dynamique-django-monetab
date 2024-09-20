from django.urls import path
from .views import download_report, index
# from .views import add
# from .views import edit

app_name = 'rapport'
urlpatterns = [
    
    path('', index, name='index'),
    path('download/', download_report, name='download')
    #path('generate_pdf/', generate_pdf, name='generate_pdf'),
    #path('generate_excel/', generate_excel, name='generate_excel'),

    # path('add', add),
    # path('edit', edit),
    
]