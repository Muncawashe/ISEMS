# reports.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponse
from .models import User, Task, Leave
from datetime import timedelta
from django.db.models import Avg

def generate_employee_report(user_id):
    # Get the employee and their tasks
    employee = User.objects.get(id=user_id)
    tasks = Task.objects.filter(assigned_to=employee, approved=True)
    leaves = Leave.objects.filter(user=employee, approved=True)
    
    # Calculate total hours worked
    total_hours_worked = (employee.last_login - employee.date_joined).total_seconds() / 3600
    
    # Calculate average performance
    avg_perf = tasks.aggregate(Avg('perfomance'))['perfomance__avg']
    
    # Create a PDF file
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setLineWidth(.3)
    p.setFont('Helvetica-Bold', 12)  # Set bold font for headers
    
    # Title
    p.drawString(30, 750, 'Employee Performance Report')
    p.drawString(30, 735, f'Employee: {employee.first_name} {employee.last_name}')
    p.drawString(30, 720, f'Total Hours Worked: {total_hours_worked:.2f}')
    p.drawString(30, 705, f'Average Performance: {avg_perf:.2f}' if avg_perf else 'Average Performance: N/A')
    
    # Task table header
    p.drawString(30, 620, 'Tasks:')
    p.drawString(30, 605, 'Title')
    p.drawString(300, 605, 'End')
    p.drawString(400, 605, 'Performance')
    
    # Task table rows
    y_task = 590
    for task in tasks:
        p.drawString(30, y_task, task.title)
        p.drawString(300, y_task, task.end.strftime('%Y-%m-%d %H:%M'))
        p.drawString(400, y_task, str(task.perfomance))
        y_task -= 15
        if y_task < 50:
            p.showPage()
            p.setFont('Helvetica-Bold', 12)  # Reset font for next page
            y_task = 750
    
    # Add space between sections
    p.drawString(30, 560, '')  # Empty line for spacing
    
    # Leave information header
    p.drawString(30, 540, 'Leave Information:')
    p.drawString(30, 525, 'Start Date')
    p.drawString(200, 525, 'End Date')
    p.drawString(400, 525, 'Reason')
    
    # Leave information rows
    y_leave = 505
    for leave in leaves:
        p.drawString(30, y_leave, f'Start Date: {leave.start.strftime("%Y-%m-%d")}')
        p.drawString(200, y_leave, f'End Date: {leave.end.strftime("%Y-%m-%d")}')
        p.drawString(400, y_leave, f'Reason: {leave.reason}')
        y_leave -= 15
        if y_leave < 50:
            p.showPage()
            p.setFont('Helvetica-Bold', 12)  # Reset font for next page
            y_leave = 750

    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer
