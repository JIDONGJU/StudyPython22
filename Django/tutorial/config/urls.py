"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 홈페이지 주소 뒤에 붙는거
    # view : 바로 보여주기
    # include : ~app.urls의 내용을 실행해라
    # views에서 함수를 만들고 urls에서 실행? 보여주기 만들고 여기와서 연결점 만들기
    path('index1/', views.index1),
    path('index2/', views.index2),
    path('first/',include('testapp.urls')),
    path('home/',include('testapp.urls')),
    path('second/',include('secondapp.urls')),
]
