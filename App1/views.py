from django.contrib.auth import authenticate, login
from django.contrib.sites import requests
from django.db.models.functions import datetime
from django.shortcuts import render, redirect

from App1.forms import RegisterForm
from App1.models import Taskdata, UserProfile


# Create your views here.
def Home(request):


    return render(request,'Home.html')
def userlogin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(Home)
    return render(request, 'login.html')
def changepsw(request):
    return render(request,'changepsw.html')
def completedtask(request):
    val = Taskdata.objects.filter(Status="completed")
    return render(request, 'Pendingtask.html', {'val': val})
def createprofile(request):
    data=UserProfile.objects.get(id=request.user.id)
    if request.method=='POST':
        phone=request.POST['Phone']
        address=request.POST['Address']
        dob=request.POST['DOB']
        pro=UserProfile.object.create(user=request.user.id,Phone=phone,Address=address,DOB=dob)
        pro.save()
        return redirect(viewprofile)
    return render(request,'createprofile.html',{'data':data})
def viewprofile(request):
    # user1=request.user
    # data=
    return render(request,'viewprofile.html')
def detailedview(request):
    val=Taskdata.objects.get(id=id)
    return render(request,'detailedview.html',{'val':val})
def forgottpsw(request):
   # if request.method=='POST':
   #     mob1=request.POST['Phone']
   #     user1=UserProfile.objects.get(Phone=mob1)
   #     if user1:
   #         url = "https://2factor.in/API/V1/03d7cbb4-4364-11ee-addf-0200cd936042/SMS/+91/AUTOGEN".format(str(mob1))
   #
   #         payload=""
   #         headers = {'content-type':'application/x-www-form-urlencoded'}
   #         response = requests.request("GET", url, headers=headers, data=payload)
   #         data=response.json()
   #         if data['Status']=='Success':
   #              return redirect(resetpsw)
   #          else:
   #            return redirect(request,'forgottpsw.html')
      return render(request,'forgottpsw.html')
def UserRegister(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect(userlogin)
        return render(request,'register.html',{'form':form})
def resetpsw(request):
    # if request.method=='POST':
    #     otp=request.POST['otp']
    #     pasw=request.POST['passw']
    #     cpsw=request.POST['cpassw']
    #     url1 = "https://2factor.in/API/V1/03d7cbb4-4364-11ee-addf-0200cd936042/SMS/VERIFY/{}/{}".format(Phone,otp)
    #     data=requests.get(url1).json()
    #     print(res)
    #     Phone=request.session.get('Phone')
    #     if data['Status']=='Success':
    #         if pasw==cpsw:
    #             user1=UserProfile.objects.get(Phone=Phone)
    #             data2=user.objects.get(id=user1.user_id)
    #             v=user.objects.get(username=data2.username)
    #             v.set_password(pasw)
    #             v.save()
    #             return redirect(userlogin)
            return render(request,'verify.html')
def updatetask(request):
    val = Taskdata.objects.get(id=id)
    val.Taskname = request.POST['Taskname']
    val.Duedate = request.POST['Duedate']
    val.Description = request.POST['Description']
    val.save()
    return render(request, 'addtask.html')
def updateprofile(request):
    return render(request,'updateprofile.html')
def Addtask(request):
    if request.method == 'POST':
        tname = request.POST['Taskname']
        due = request.POST['Duedate']
        des = request.POST['Description']
        user = request.user.id
        Startdate = datetime.datetime.today()
        val = Taskdata.objects.create(user_id=user, Taskname=tname, Startdate=Startdate, Duedate=due, Description=des,
                                      Status='pending')
        val.save()
        return redirect(Pendingtask)
    return render(request, 'addtask.html')
def Pendingtask(request):
    val = Taskdata.objects.filter(Status="pending").order_by("Duedate")
    return render(request, 'Pendingtask.html', {'val': val})
def delete(request,id):
    val=Taskdata.objects.get(id=id)
    val.delete()
    return redirect('Pendingtask.html')
def edit(request,id):
    val=Taskdata.objects.get(id=id)
    context={'val':val}
    return render(request,'Addtask.html',context)
def add(request,id):
    val=Taskdata.objects.get(id=id)
    val.add()
    return redirect('completedtask.html')





