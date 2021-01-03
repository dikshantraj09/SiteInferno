from django.shortcuts import render
from .models import TeamMembers,Contact,Sponsor
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'HOME/home.html')

def team(request):
    teammem=TeamMembers.objects.all()
    memid=TeamMembers.objects.values('sno')
    messages.success(request, 'Welcome to our Team Page')

    return render(request,'HOME/team.html',{'teaminferno':teammem,'memid':memid})

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your details has been saved')
    return render(request, 'HOME/contact.html')


def urc(request):
    return render(request,'HOME/urc.html')

def irdc(request):
    return render(request,'HOME/irdc.html')

def project(request):
    return render(request,'HOME/project.html')

def sponsor(request):
    sponsors=Sponsor.objects.all()
    return render(request,'HOME/sponsor.html',{'sponsors':sponsors})

