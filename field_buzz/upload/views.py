from django.shortcuts import render
from rest_framework import viewsets
from .models import UploadInfo
from .serializers import UploadInfoSerializer

# Create your views here.
class UploadView(viewsets.ModelViewSet):
    queryset = UploadInfo.objects.all()
    serializer_class = UploadInfoSerializer