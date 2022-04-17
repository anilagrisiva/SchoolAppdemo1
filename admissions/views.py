from django.shortcuts import render
from admissions.forms import admiModelForm
from django.http import HttpResponse
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView,View
from admissions.models import StaffList,Students
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

def sendsms(a,b):
    per = Students.objects.filter(phoneno=a) &  Students.objects.filter(dateofbirth=b)
    url = "https://www.fast2sms.com/dev/bulkV2"
    print(per)
    id = 0
    for i in per:
        print(i)
        id=i.id
    message = id
    message2 = b
    number = a

    no1="sender_id=TXTIND&message=Welcome to CoolTech your id and password is "
    no2=str(message)
    no5=" and "
    no6=str(message2)
    no3 = "&route=v3&numbers="
    no4 =str(number)
    payload = no1+no2+no5+no6+no3+no4
    headers = {
        'authorization': "UiHB1JcQwyPTs0RvAV42K6gL3jSrdpz9EX7al5nmqhFbZIfOYMcOKvQekIJxipnoUT9sMqYflDuABFVt",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return "okkk";




def addNewAdmision(request):
    form = admiModelForm
    king = {"form":form}

    if request.method == "POST":
        form = admiModelForm(request.POST)
        if form.is_valid():
            form.save()
            a=str(form["phoneno"])
            a=a.split(" ")
            a=a[3]
            b=str(form["dateofbirth"])
            b=b.split(" ")
            b=b[3]
            a=a.replace("value=","")
            a=a.replace("\"","")
            b=b.replace("value=","")
            b=b.replace("\"","")
            b=datetime.strptime(b, '%d/%m/%Y')
            print(a,b)
            n=sendsms(a,b)
        return admisuccess(request);

    return render(request,'admissions/add-admission.html',king)



@login_required
def admisuccess(request):
    return render(request,'admissions/status-page.html')

# Create your views here.

class addNewTeacher(View):
    def get(self,request):
        return HttpResponse("<h1>this is Class Based View</h1>")



class getStaffDetails(ListView):
    model = StaffList
    #default context_name = model_list = StaffList_list
    #default templetname = context_object_name.html = StaffList_list.html


class getoneStaff(DetailView):
    model = StaffList


class addStaff(CreateView):
    model = StaffList
    fields = ('name','subject','phone_No','experience')


class updateStaff(UpdateView):
    model = StaffList
    fields = ('name','phone_No','subject')


class deleteStaff(DeleteView):
    model = StaffList
    success_url = reverse_lazy('teachersList')
