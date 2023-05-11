from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='signin')
def Home(request):
    userdate = Biodata.objects.all()
    context = {"data":userdate}
    return render(request,'home.html',context)


@login_required(login_url='signin')
def Create(request):

    if request.method == 'POST':
       
        userdate = Biodata.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'])
        userdate.save()
        

    return render(request,'create.html')


@login_required(login_url='signin')
def Update(request,id):
    # get user record with pk as id  
    data = get_object_or_404(Biodata, pk=id)

    # form instance will be what record is been read
    form = BiodataForm(instance=data)

    if request.method == "POST":
        # form data is what ever is been sent in the form 
        form = BiodataForm(request.POST, instance=data)
        # if the form is valid the form data should be saved to our db
        if form.is_valid():
            form.save()
            # then return to our home page
            return redirect ('home')
    context = {
        "form":form
    }
    return render(request, 'updateform.html', context)


@login_required(login_url='signin')
def Delete(request,id):
    # get object delete and redirect to home page
     data = get_object_or_404(Biodata, pk=id)
     data.delete()
     return redirect ('home')

     