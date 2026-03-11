from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import User,Course

# Create your views here.

login_status = False
username = None
role = None

login_failed = False

def home_page(req):
    return render(req,'home.html',{'status':login_failed})

def admin_dashboard(req):
    u_name = req.POST.get('un')
    u_pass = req.POST.get('up')
    u1 = User.objects.filter(username = u_name, password = u_pass, role = 'admin').exists()
    if u1 == True:
        global username,role,login_status
        username = u_name
        role = 'admin'
        login_status = True
        all_students = User.objects.filter(role = 'student')
        return render(req,'dashboard.html',{'name':u_name,'students':all_students})
    else:
        global login_failed
        login_failed = True
        return redirect('/',{'status':login_failed})
    
def create_student(req):
    if req.method != 'POST': 
        if role == 'admin' and login_status == True:
            return render(req,'create_student.html')
        else:
            return redirect('/')
    else:
        u_name = req.POST.get('un')
        u_pass = req.POST.get('up')
        u_addr = req.POST.get('addr')
        u_ph = req.POST.get('uph')

    User.objects.create(
        username = u_name,
        address = u_addr,
        phone_number = u_ph,
        password = u_pass,
        role = 'student'
    )
    return redirect('/')

def update_student(req,input_id):
    if req.method == 'POST':
        name = req.POST.get('un')
        u_pass = req.POST.get('up')
        addr = req.POST.get('addr')
        phn = req.POST.get('uph')
        obj = get_object_or_404(User,id = input_id)
        obj.username = name
        obj.password = u_pass
        obj.address = addr
        obj.phone_number = phn
        obj.save()
        return redirect('/')

    obj = get_object_or_404(User,id = input_id)
    res = {}
    res['u_name'] = obj.username
    res['u_pass'] = obj.password
    res['addr'] = obj.address
    res['phn'] = obj.phone_number
    return render(req,'update_student.html',res)

def delete_student(req,input_id):
    obj = get_object_or_404(User,id = input_id)
    obj.delete()
    return redirect('/')

def create_course(req):
    if req.method == 'POST':
        course = req.POST.get('c_name')
        desc = req.POST.get('desc')
        Course.objects.create(
            name = course,
            description = desc
        )
        return redirect('/')
    return render(req,'create_course.html')

def add_course_student(req):
    if req.method == 'POST':
        c_id = req.POST.get('c_id')
        s_id = req.POST.get('s_id')
        if Course.objects.filter(id = c_id).exists() and User.objects.filter(id = s_id, role = 'student').exists():
            course = Course.objects.get(id = c_id)
            new_student = User.objects.get(id = s_id)
            course.student.add(new_student)
            course.save()
            return redirect('/')
    all_students = User.objects.filter(role = 'student')
    all_courses = Course.objects.all()
    return render(req,'associate.html',{'students':all_students,'courses':all_courses})