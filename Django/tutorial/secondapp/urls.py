from django.urls import include, path
from . import views

urlpatterns = [
    path('insert/', views.insert),
    path('main/', views.main),
    path('lprod_list/', views.view_Lprod_list),
    path('lprod/', views.view_Lprod),
]
