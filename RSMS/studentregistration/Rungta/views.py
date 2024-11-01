from django.shortcuts import render,HttpResponse,redirect
from . models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def logout_view(request):
    logout(request)  
    return redirect('login') 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required
def show(request):
    
    return render(request,"home.html")
@login_required
def all_stu(request):
    stud = Student.objects.all()
    context = {
        'studs': stud

    }
    
    return render(request,'viewstudent.html',context)
@login_required
def register(request):
    if request.method == 'POST':
        s_name = request.POST['s_name']
        s_fathername = request.POST['s_fathername']
        s_mothername = request.POST['s_mothername']
        s_addr = request.POST['s_addr']
        s_school = request.POST['s_school']
        s_email = request.POST['s_email']
        s_gender = request.POST['s_gender']
        s_class = request.POST['s_class']
        new_stu = Student(s_name=s_name, s_fathername=s_fathername, s_mothername=s_mothername, s_addr=s_addr, s_school=s_school, s_email=s_email, s_gender=s_gender,s_class=s_class)
        new_stu.save()
        messages.success(request,"Student has been added succeffuly")
        return redirect('reg')
        
    elif request.method =='GET':
        return render(request,'register.html')        
    else:
        return HttpResponse("Exception Occured")
    
@login_required
def search_stu(request):
    if request.method == 'POST':
       s_name = request.POST['s_name']
       s_fathername = request.POST['s_fathername']
       s_mothername = request.POST['s_mothername']
       stud = Student.objects.all()
       if s_name:
            studs = stud.filter (s_name__icontains = s_name)
       if s_fathername:
            studs = stud.filter(s_fathername__icontains = s_fathername)     


       if s_mothername:
            studs = stud.filter(s_mothername__icontains = s_mothername)
       context = {
                'studs': studs
                
           
        }
            
       return render(request, 'viewstudent.html', context)
       
    elif request.method == 'GET':            

          return render(request,'search_student.html')
    else:
            return HttpResponse('An eception Occured')
    
@login_required
def delete_stud(request):
    
    studs = Student.objects.all()
    context = {
                'studs': studs
                
           
        }
    
    return render(request,'delete_student.html',context)
@login_required
def delete_studs(request,stud_id):
    if  request.method=="POST":
        
        try:
            stu_to_be_removed = Student.objects.get(id=stud_id)
            stu_to_be_removed.delete()
            
            messages.success(request,"Student has been delete succeffuly")
            return redirect('delete_stud')
            
        except:
            return HttpResponse("Please Enter valid student id")
    studs = Student.objects.get(id=stud_id)
    studentname=studs.s_name
    context = {
                'studs': studentname
                
           
        }
    
    return render(request,'delete.html',context)



@login_required
def update_student(request,id):
    student = Student.objects.get(id=id)
    context = {
        "student":student,
    }
    return render(request,'update_student_details.html',context)
@login_required
def STUDENT_UPDATE(request):
        if request.method == 'POST':
         
          student_id = request.POST.get('student_id')
          s_name = request.POST['s_name']
          s_fathername = request.POST['s_fathername']
          s_mothername = request.POST['s_mothername']
          s_addr = request.POST['s_addr']
          s_school = request.POST['s_school']
          s_email = request.POST['s_email']
          s_gender = request.POST['s_gender']
          s_class = request.POST['s_class']   

          student =Student.objects.get(id=student_id) 
          student.s_name =s_name
          student.s_fathername =s_fathername
          student.s_mothername =s_mothername
          student.s_addr =s_addr
          student.s_school =s_school
          student.s_email =s_email
          student.s_gender =s_gender 
          student.s_class =s_class 
          student.save()   
          messages.success(request,"Your student profile has been updated successfully")
          return redirect('delete_stud')
    
        return render(request, 'update_student_details.html')
    
        
        
        