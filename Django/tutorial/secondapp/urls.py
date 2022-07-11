from django.urls import include, path
from . import views

urlpatterns = [
    path('insert/', views.insert),
    path('main/', views.main),
]
