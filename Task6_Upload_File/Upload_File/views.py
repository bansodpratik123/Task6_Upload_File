from django.shortcuts import render,redirect
from .models import Cities
from .forms import CitiesModelForm

# Create your views here.

def homepage(request):
    return render(request,'Homepage.html',{})


def uploadIamage(request):
    form=CitiesModelForm()
    if request.method=='POST':
        form=CitiesModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')

    return render(request, 'UploadImage.html',{'form':form})

def showImage(request):
    img=Cities.objects.all()
    return render(request, 'ShowImage.html',{'img':img})