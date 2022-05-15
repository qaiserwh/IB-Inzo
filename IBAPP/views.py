from multiprocessing import *
from.models import *
from.forms import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

# def form(request):
#     if request.method =='POST':
#         Att= OpinionForm(request.POST)
#         if Att.is_valid():
#             Att.save()
#             return  redirect('about')
# 
#     context={
#         'forms':Opinion.objects.all(),
#         'forms': OpinionForm(),
#     }
# 
#     return render(request,'about.html',context)
def index(request):
    context={
        # 'y':Offer.objects.all(),
        'Ibcard':IbAccountPage1.objects.all(),
        # 'thecourse':Course.objects.all(),
        
    }
    return render(request,'index.html',context)
############
def index1(request):
    context={
    
        'page2':IbAccountPage2.objects.all(),
       
        
    }
    return render(request,'index1.html',context)

def index2(request):
    context={

        'page3':IbAccountPage3.objects.all(),
 
        
    }
    return render(request,'index2.html',context)########
########################################################
def index3(request):
    context={
      
        'page4':IbAccountPage4.objects.all(),

        
    }
    return render(request,'index3.html',context)

def index4(request):
    context={
  
        'page5':IbAccountPage5.objects.all(),
       
        
    }
    return render(request,'index4.html',context)

def offers(request):
    context={
       # 'y':Offer.objects.all(),
       # 'dat':IbAccountPage1.objects.all(),
        'y':Offer.objects.all(),
        
    }
    return render(request,'offers.html',context)
       
def course(request):
    context={
        'thecourse':Course.objects.all()
    }
    return render(request,'course.html',context)

def about(request):
    Atts= None
    if request.method =='POST':
            Att= OpinionForm(request.POST)
            if Att.is_valid():
                Att.save(commit=True)
                return  redirect('about')

    context={
            'des':About.objects.all(),
            'op':Opinion.objects.all(),
            'forms': OpinionForm(),
    }

    return render(request,'about.html',context)

def education(request):
    context={

        'sero':Education.objects.all()

    }
    return render(request,'sero.html',context)