The System is created using Django, html and css
installed modules django-import_export for exporting and importing database information
python manage.py runserver

Run python manage.py createsuperuser to create an admin account.
admin can add employees to the system and the default password for employees is 123.
admin and employees can log into the system as per their roles.
admin can assign tasks to employee.
employee can view tasks and set them to completed once completed.
the completed tasks will appear on the employee profile on the admin's portal for performance measurement.

Design:
The system can be run on a local network so everything is database oriented.
admin and regular users are distinguished through is_superuser and is_staff fields in the users table.
Database tables.
Users - storing all users.
Department -- storing departments.
Role -- storing user roles in the department.
Session -- keeps track of user login and log out information to calculate the amount of time they work.
Tasks -- storing taks and the employee assigned the task.
Leave -- storing leave applications and a approved field once the admin approves the application.
Message -- storing messages from admin to employees, employees should also be able to sent messages to admin.
