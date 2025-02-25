from django.shortcuts import render,redirect
from store.models import student
from django.http import HttpResponse

def signup(request):
    return render(request, 'signup.html')

def myaction(request):
    email = request.POST.get('email')
    if student.objects.filter(email=email).exists():
        return HttpResponse('Email already exists')
    else:
        if request.method == "POST":
            stu = student()
            stu.fname = request.POST.get('fname')
            stu.lname = request.POST.get('lname')
            stu.address = request.POST.get('address')
            stu.pin = request.POST.get('pin')
            stu.city = request.POST.get('city')
            stu.state = request.POST.get('state')
            stu.password = request.POST.get('password')
            stu.email = request.POST.get('email')
            stu.phone_no = request.POST.get('phone')
            stu.father_name = request.POST.get('father_name')
            stu.mother_name = request.POST.get('mother_name')
            stu.tenth_marks = request.POST.get('tenth_marks')
            stu.twelth_marks = request.POST.get('twelth_marks')
            stu.subject = request.POST.get('subject')
            stu.save()
            return HttpResponse(
                "<script>alert('Registration Successful');window.location.href='/show'</script>")
        else:
            return HttpResponse('Error')

def login(request):
    return render(request, 'login.html')

def userlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if student.objects.filter(email=email, password=password, isApproved=True).exists():
        return HttpResponse('Login Successful')
    else:
        return HttpResponse('Login Failed')


def show(request):
    stu = student.objects.all()
    return render(request, 'show.html', {'stu': stu})

def dele(request,id):
    stu = student.objects.get(id=id)
    stu.delete()
    return redirect ('/show')

def edit(request,id):
    stu = student.objects.get(id=id)
    return render(request, 'edit.html', {'stu': stu})

def upd(request,id):
    stu = student.objects.get(id=id)
    stu.fname = request.POST['fname']
    stu.lname = request.POST['email']
    stu.phone_no = request.POST['phone']
    stu.save()
    return redirect('/show')


def approve(request, id):
    stu = student.objects.get(id=id)
    stu.isApproved = True
    stu.save()
    return redirect('/show')

def decline(request, id):
    stu = student.objects.get(id=id)
    stu.isApproved = False
    stu.save()
    return redirect('/show')