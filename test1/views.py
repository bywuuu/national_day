import os

from django.shortcuts import render

# Create your views here.
def rendermy(request):
    print(os.path.curdir)
    return render(request,'test1/feelings.html')