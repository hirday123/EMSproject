from django.shortcuts import render
from django.http import JsonResponse
from .models import AdminDataBase

def homePageView(request):
    return render(request,'home.html')


def aregistration(request):
     # data = request.POST
    # Fname = data.values()
    # data1 = {
    #     'key':list(Fname)
    # }
    # print(data)
    # print(Fname)
    # print(data1)
    # print(data1.keys())
    # print(data1.values())
    
    # return JsonResponse(data1)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        user = AdminDataBase.objects.filter(email=email)
        if user:
            msg= "User already exist"
            return render(request,'aregistration.html',{'msg':msg})
        else:
            newdatainsert = AdminDataBase.objects.create(firstname=fname,email=email,lastname=lname,contact=contact,password=password)
            return render(request,'home.html')
    return render(request,'aregistration.html')

    
    
def adminloginpage(request):
     return render(request,'adminloginpage.html')
 
def uregistration(request):
     return render(request,'uregistration.html')

def userloginpage(request):
     return render(request,'userloginpage.html')