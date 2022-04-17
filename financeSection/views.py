from django.shortcuts import render
from admissions.models import Students
from admissions.forms import admiModelForm
# Create your views here.

def paymetSection(request):
    deta = Students.objects.all()
    send= {"deta":deta}
    return render(request,'finance/finance.html',send);



def deleteYourDetails(request,id) :
    s = Students.objects.get(id=id)
    s.delete()
    return paymetSection(request);



def updateYourDetails(request,id):
    s=Students.objects.get(id=id)
    form = admiModelForm(instance=s)
    dict={"form":form}

    if request.method=='POST':
        form = admiModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return paymetSection(request)
    return render(request,'admissions/update-details.html',dict);
