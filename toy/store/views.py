from django.shortcuts import render,redirect
from store.models import student
from django.http import HttpResponse

def signup(request):
    return render(request, 'signup.html')

def myaction(request):
    if request.method == "POST":
        stu = student()
        stu.fname = request.POST.get('fname')
        stu.lname = request.POST.get('lname')
        stu.address = request.POST.get('address')
        stu.pin = request.POST.get('pin')
        stu.city = request.POST.get('city')
        stu.state = request.POST.get('state')
        stu.email = request.POST.get('email')
        stu.phone_no = request.POST.get('phone')
        stu.father_name = request.POST.get('father_name')
        stu.mother_name = request.POST.get('mother_name')
        stu.tenth_marks = request.POST.get('tenth_marks')
        stu.twelth_marks = request.POST.get('twelth_marks')
        stu.subject = request.POST.get('subject')
        stu.save()
        return redirect('/show')
    else:
        return HttpResponse('Error')
    
    
def show(request):
    stu = student.objects.all()
    return render(request, 'show.html', {'stu': stu})

def dele(request,id):
    stu = student.objects.get(id=id)
    stu.delete()
    return redirect ('/show')