from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import csv
from io import BytesIO
from reportlab.pdfgen import canvas
from student.models.student_model import StudentModel
from teacher.models.teacher_model import TeacherModel
from user.models.user_model import CustomUserModel
from openpyxl import Workbook

# Create your views here.
@login_required(login_url='login:login')
def index(request):
    return render(request, "rapport/index.html")

login_required(login_url='login:login')
def download_report(request):
    report_type = request.POST.get('report_type')
    format_type = request.POST.get('format')

    # Sélectionner les données en fonction du type de rapport
    if report_type == 'students':
        data = StudentModel.objects.all()
    elif report_type == 'teachers':
        data = TeacherModel.objects.all()
    elif report_type == 'users':
        data = CustomUserModel.objects.all()    
    else:
        return HttpResponse("Type de rapport invalide", status=400)

    # Vérifier le format et générer le rapport en conséquence
    if format_type == 'pdf':
        return generate_pdf(data, report_type)
    elif format_type == 'excel':
        return generate_excel(data, report_type)
    else:
        return HttpResponse("Format non supporté", status=400)




def generate_pdf(data, report_type):

    
    # Create a BytesIO buffer to hold the PDF
    buffer = BytesIO()
    
    # Create a PDF object using the buffer
    pdf = canvas.Canvas(buffer)
    
    # Fetch data from the database
    
    # Example: add text or content to the PDF
    pdf.drawString(100, 800, "Data Report")
    
    y_position = 750  # Starting Y position for data entries
    
    for record in data:
        if report_type == 'users':
            pdf.drawString(100, y_position, f"Record: {record.pseudo} - Value: {record.creat_at}")
        else:
        # You can format the data as needed (e.g., record.name, record.value)
            pdf.drawString(100, y_position, f"Record: {record.last_name} - Value: {record.first_name}")
        y_position -= 20  # Move down for the next line
    
    # Finalize the PDF
    pdf.showPage()
    pdf.save()
    
    # Get the value of the BytesIO buffer and create an HTTP response
    pdf_output = buffer.getvalue()
    buffer.close()
    
    response = HttpResponse(pdf_output, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{report_type}.pdf"'
    
    return response

def generate_excel(data, report_type):
    # Create an in-memory workbook
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Data Report"
    
    # Fetch data from the database
    
    # Add headers (if needed)
    worksheet.append(["ID", "name", "last_name"])
    # Write data to Excel
    for record in data:
        if report_type == 'users':
            worksheet.append([record.id, record.pseudo])
        else:    
            worksheet.append([record.id, record.first_name, record.last_name])
    
    # Prepare the response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{report_type}.xlsx"'
    
    # Save the workbook to the response
    workbook.save(response)
    
    return response