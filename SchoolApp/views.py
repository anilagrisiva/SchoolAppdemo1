from django.shortcuts import render




def home(request):
    return render(request,"admissions/main-page.html")
