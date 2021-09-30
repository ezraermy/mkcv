from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Employee, CVmaker
from .forms import ApplyForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        employees=Employee.objects.filter(cvmaker__title=request.user.username)
        context={
            'employees':employees,
        }
        return render(request,'cv/openings.html',context)
    else:
        cvmakers=CVmaker.objects.all()
        context={
            'cvmakers':cvmakers,
        }
        return render(request,'cv/openings.html',context)

def apply(request):
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('success')
    context = {
        'form': form,
    }
    return render(request, 'cv/apply.html', context)

def success(request):
    return render(request, 'cv/success.html')