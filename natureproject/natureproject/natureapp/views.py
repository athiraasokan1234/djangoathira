

from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from.models import purchase
# Create your views here.
def demo(request):
    obj=place.objects.all()
    abj=purchase.objects.all()

    return render(request,"index.html",{'result':obj,'results':abj})
#def calculate(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #res=x+y
    #rex=x-y
    #sol=x*y
    #div=x/y
    #return render(request, "result.html", {'result': res,'result2':rex,'result3':sol,'result4':div})


