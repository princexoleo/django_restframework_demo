from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('uploadinfo', views.UploadView)

urlpatterns = [
    #path('', include('languages.urls'))
    path('', include(router.urls))
    
]
