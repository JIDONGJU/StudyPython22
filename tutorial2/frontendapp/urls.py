from django.urls import path

from . import views

urlpatterns = [
    path("sample01/", views.sample_01),
    path("index01/", views.index_01),
    path("index02_css/", views.index_02),
    path("index03_css/", views.index_03),
    path("index04_css/", views.index_04),
    path("index05_css/", views.index_05),
    path("index06_css/", views.index_06),
]
