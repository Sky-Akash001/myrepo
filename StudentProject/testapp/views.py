from django.shortcuts import render
import datetime
from .models import Contact
from django.http import HttpResponse

# Create your views here.
date = datetime.datetime.now()
h = date.strftime("%Y")
def display(request):
    return render(request,'testapp/home.html',{'h':h})

def about(request):
    return render(request,'testapp/about.html')

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return render(request,'testapp/contactgreet.html')
    return render(request,'testapp/contact.html')

def python(request):
    return render(request,'testapp/python.html')

def java(request):
    return render(request,'testapp/java.html')

def web(request):
    return render(request,'testapp/web.html')

def android(request):
    return render(request,'testapp/android.html')

def prog(request):
    return render(request,'testapp/prog.html')

def htcss(request):
    return render(request,'testapp/htcss.html')

def quiz(request):
    return render(request,'testapp/quiz.html')

######################################################################################Comming Soon###############################################################
def c(request):
    return render(request,'testapp/comming_soon.html')

def j(request):
    return render(request,'testapp/comming_soon.html')
######################################################################################Compiler####################################################################
import sys
def index(request):
    return render(request,'testapp/compiler.html')

def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt','w')


            exec(codeareadata)

            sys.stdout.close()
            sys.stdout = original_stdout
            print("H1")
            print("j2)")

            output = open('file.txt','r').read()

        except Exception as e:
            sys.stdout = original_stdout
            output = e
    return render(request,'testapp/compiler.html', {'code':codeareadata, 'output':output})
