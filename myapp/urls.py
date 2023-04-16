from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/<str:name>/<str:email>', views.success, name='success'),
]
