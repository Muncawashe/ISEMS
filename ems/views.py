from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Department, Role, Events, User
from django.db.models import Q
import csv
from io import TextIOWrapper


def index(request):
    if request.user.is_superuser == True:
        return render(request, "superuser.html")
    elif request.user.is_staff==True:
        return render(request, "staff.html")
    else:
        return render(request, "staff.html")
            

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

def all_user(request):
    queryset = User.objects.all()
    context = {"employees":queryset}
    return render(request, "all_user.html", context)

def add_user(request):
    queryset = Role.objects.all()
    queryset1 = Department.objects.all()
    context = {"roles":queryset, "depts":queryset1}

    if request.method == "POST":
        f_name = request.POST['first_name']
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        username = request.POST.get('username')

        User.objects.create(first_name = f_name, last_name = l_name, phone = phone, email = email, password = password, username = username, is_staff = True)
        # User.objects.create(first_name = f_name, last_name = l_name, dept_id = dept, role_id = role, phone = phone, email = email, password = password, username = username, is_staff = True)
        return HttpResponse("User added successfully")
    
    elif request.method == "GET":
        return render(request, "add_user.html", context)
    
    else:
        HttpResponse("invalid request")

def delete_user_id(request,user_id):
        try:
            obj =User.objects.get(id = user_id)
            obj.delete()
            queryset =User.objects.all()
            context = {"employees":queryset}

            return render(request, "all_user.html", context)
        except:
            return HttpResponse("Please choose the valid User")
        
def view_profile(request,user_id):

    if request.method == "GET":
        if user_id:
            queryset = User.objects.get(id = user_id)
            # queryset2 = User.objects.all()
            context = {"employees":queryset}
            return render(request, "emp_profile.html",context)
        
def update_user(request,user_id):
    queryset = Role.objects.all()
    queryset1 = Department.objects.all()

    if request.method == "GET":
        if user_id:
            queryset = User.objects.get(id = user_id)
            context = {"roles":queryset, "depts":queryset1}
            return render(request, "update_user.html",context)
        
    if request.method == "POST":
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        dept_id = request.POST.get("emp_dept")
        role_id = request.POST.get("emp_role")
        phone = request.POST.get("emp_phone")
        empid = request.POST.get("emp_id")
        skills = request.POST.get("emp_skills")
        salary = request.POST.get("emp_salary")
        bonus = request.POST.get("emp_bonus")
        try:
            emp_obj = User.objects.get(id=user_id)
            emp_obj.first_name = fname
            emp_obj.last_name = lname
            emp_obj.dept.id = dept_id
            emp_obj.role.id = role_id
            emp_obj.phone = phone
            emp_obj.emp_id = empid
            emp_obj.skills = skills
            emp_obj.salary = salary
            emp_obj.bonus = bonus
            emp_obj.dept.save()
            emp_obj.save()
            
            queryset = User.objects.all()
            context = {"emps":queryset}
            return render(request, "all_user.html", context)
        except:
            return HttpResponse("please enter valid data")
    else:
        return HttpResponse("invalid request")

def bulk_upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        if file.name.endswith('.csv'):
            text_file = TextIOWrapper(file, encoding='utf-8')
            reader = csv.reader(text_file)
            headers = next(reader)

            for row in reader:
                data = {
                    'first_name' : row[0],
                    'last_name' : row[1],
                    'email' : row[2],
                    'dept_id' : row[3],
                    'role_id' : row[4],
                    'phone' : row[5], 
                    'username' : row[6], 
                    'password' : row[7], 
                }
                employee = User.objects.create(**data)
                employee.save()
            return HttpResponse("Bulk add via CSV Successfully")
        else:
            return HttpResponse("please enter valid data")
    return render(request, 'bulk_upload.html')

def filter_user(request):
    if request.method == "POST":
        name = request.POST.get('first_name')
        role = request.POST.get('emp_role')
        dept = request.POST.get('emp_dept')

        employees = User.objects.all()
        if name:
            employees = employees.filter(Q(first_name__icontains = name) | Q(last_name__icontains=name))
        if role:
            employees = employees.filter(role__name__icontains = role)
        if dept:
            employees = employees.filter(dept__name__icontains = dept)

        context = {"employees":employees}
        return render(request, "all_user.html", context)
    elif request.method == "GET":
        return render(request, "search_user.html" )
    else:
        return HttpResponse("An exception occured")

def create_event(request, user_id):
    if user_id:
            queryset = User.objects.get(id = user_id)
            context = {"employee":queryset}
            return render(request, "create_event.html",context)
    
    if request.method == "POST":
        name = request.POST['name']
        start = request.POST.get('start')
        end = request.POST.get('end')

        Events.objects.create()
        return HttpResponse("Schedule Event added successfully")  
    else:
        HttpResponse("invalid request")
