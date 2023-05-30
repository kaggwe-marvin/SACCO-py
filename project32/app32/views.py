from django.shortcuts import render
from django.urls import reverse
from .forms import Application, Contact
from .models import applicant, contacts


# Create your views here.

def home(request):
    photos = ['1.jpg', '2.jpg', '3.jpg']
    url = reverse('app32:home')
    context = {'photos': photos, 'url': url}
    return render(request, 'index.html', context)
    

def about(request):
    url = reverse('app32:about')
    msg = contacts.objects.all().order_by('-id')
    context = {'url': url, 'msg':msg}
    return render(request, 'about.html',context)


def apply(request):
    url = reverse('app32:apply')
    if request.method == 'POST':
        form = Application(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'approval.html')
    else:
        form = Application()
    context = {'url': url, 'form':form}
    return render(request, 'apply.html',context)


def contact(request):
    url = reverse('app32:contact')
    if request.method == 'POST' :
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html')
    else:
        form = Contact()
    
    context = {'url': url, 'form':form}
    return render(request, 'contact.html',context)

def approval(request):
    url = reverse('app32:approval')
    approve = applicant.objects.all().order_by('-id')
    context = {'url': url, 'approve': approve}
    return render(request, 'approval.html',context)
