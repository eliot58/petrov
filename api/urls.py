from django.urls import path
from .views import *

urlpatterns = [
    path('bonus/', bonus),
    path('update_data/', update_data)
]