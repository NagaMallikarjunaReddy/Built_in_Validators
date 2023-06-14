from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert(request):
    to=Topicform()
    d={'to':to}
    if request.method=='POST':
        tfo=Topicform(request.POST)
        if tfo.is_valid():
            tfo.save()
            return HttpResponse('data inserted')
        else:
            return HttpResponse('data is not valid')
    return render(request,'topic.html',d)