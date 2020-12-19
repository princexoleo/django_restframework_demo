from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework import viewsets
from .models import UploadInfo
from .serializers import UploadInfoSerializer
import requests as req

# Create your views here.
class UploadView(viewsets.ModelViewSet):
    queryset = UploadInfo.objects.all()
    serializer_class = UploadInfoSerializer


def login_view(request):
    ## 
    if request.method =='POST':
        user_email =  request.POST.get('user_email')  #"mzleon.cse@gmail.com"
        user_password =   request.POST.get('user_password')  #"o1NmBzk80"
        api_url = "https://recruitment.fisdev.com/api/login/"
        print(user_email, user_password)
        api_payload = {
            'username' : user_email,
            'password' : user_password
        }
        x = req.post(api_url, data = api_payload)
        res_data = x.json()
        token = res_data['token']
        print(res_data)
        print(token)
        return HttpResponseRedirect('/uploadinfo')
    else:
        print("Credential Failed !!")
        return render(request, 'login.html', {'title': "Login Page for Authentication"})
        
    return render(request, 'login.html', {'title': "Login Page for Authentication"})