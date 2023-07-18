from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from App.forms import *
from App.models import *

def mediafiles(request):
    MFO=ProfileForm()
    d={'MFO':MFO}
    if request.method=='POST':
        MFD=ProfileForm(request.POST)
        if MFD.is_valid():
            print(str(MFD.cleaned_data))
            return HttpResponse('Valid Form Data Recieved')
        else:
            return HttpResponse('Invalid Form Data')
    return render(request,'mediafiles.html',d)