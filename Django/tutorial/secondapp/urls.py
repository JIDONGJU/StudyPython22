
from django.urls import include, path
from . import views

urlpatterns = [
    path('main/', views.main),
]
