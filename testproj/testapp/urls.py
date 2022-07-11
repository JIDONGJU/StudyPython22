from django.urls import path
from . import views

urlpatterns = [
    path('oneshow/', views.oneshow),
    path('show/', views.show),
    path('insert/', views.insert),
    path('index1/', views.index1),
]
