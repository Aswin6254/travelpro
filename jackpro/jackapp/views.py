


from django.shortcuts import render
from . models import place
from . models import new
def demo(request):
    obj = place.objects.all()
    obj01 = new.objects.all()
    return render(request,'index.html',{'result':obj,'result01':obj01})