from django.urls import path
from . import views

urlpatterns = [
    path('show4/', views.show4),
    path('show3/', views.show3),
    path('show2/', views.show2),
    path('oneshow/', views.oneshow),
    path('show/', views.show),
    path('insert/', views.insert),
    path('index1/', views.index1),
]
