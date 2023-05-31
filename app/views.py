from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a':20,}
    return render(request,'conditions.html',context=d)
def statements(request):
     d={'a':10,'b':20}
     return render(request,'statements.html',context=d)


def python(request):
     d={'a':300,'b':30,'c':900}
     return render(request,'python.html',context=d)
def Nested(request):
     d={'a':500,'b':100,'c':200}
     return render(request,'Nested.html',context=d)
     
def loop(request):
     d={'name':'sahasra'}
     return render(request,'loop.html',context=d)
       



















