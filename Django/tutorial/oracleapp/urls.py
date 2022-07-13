from django.urls import path
from . import views

urlpatterns = [
    path('member/', views.view_Member),
    path('memberlist/', views.view_memberlist),
    path('test/', views.test),
    path('cart_list/', views.view_cart_list),
    path('cart/', views.view_cart),
    path('cart_insert/', views.set_Cart_insert),
    path('prod_list/', views.view_lprod_list),
    path('testdict/', views.testDict),
    path('cart_list_dict/', views.view_cart_list),
    path('cart_delete/', views.view_Cart_delete),
    path('cart_update_form/', views.view_Cart_update),
]