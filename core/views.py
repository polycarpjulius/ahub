from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def Home(request):
    userdate = Biodata.objects.all()
    context = {"data":userdate}
    return render(request,'home.html',context)


def Create(request):

    if request.method == 'POST':
       
        userdate = Biodata.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'])
        userdate.save()

    return render(request,'create.html')
