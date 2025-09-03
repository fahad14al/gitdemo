from django.shortcuts import render, redirect
from .models import Employee, Contact
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    employees = Employee.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Thank you for messaging us</h1>")
    else:
        form = ContactForm()
    
    context = {
        'employees': employees,
        'form': form
    }
    
    return render(request, 'index.html', context)

def trainer(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'trainer.html', context)

def whyus(request):
    return render(request, 'why.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Thank you for messaging us</h1>")
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'contact.html', context)









