
from django.contrib import admin
from django.urls import include, path

from chi2app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("test/", views.test),
    path("dbtest/", views.view_Cart_List),
    path("create_test/", views.createTable),
    path("insert_test/", views.set_Survey_Insert_test),
    path("list/", views.view_Survey_List),
    path("survey/", views.view_Servey),
    path("insert/", views.set_Survey_Insert),
]
