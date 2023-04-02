 
from django.urls import path
from .views_api import *

urlpatterns = [
    path('login/', LoginView),#did not work when used as LoginView
    
    path('register/', RegisterView)
]  