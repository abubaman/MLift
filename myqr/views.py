from django.shortcuts import render
#import qrcode
import os

def myqr(request):
    filename=request.user.username + ".png"
    url = os.path.join('qrcode',filename)
    context = {
        'username' : request.user.username, 
        'qrurl' : url
    }
    return render(request, 'myqr.html',context)

# Create your views here.