from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('uploadinfo', views.UploadView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login_view, name='login')
    
]
