from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from testapp.models import Curriculum
from .models import Curriculum
from .models import Course


def index1(request):
    return HttpResponse('<p>안녕하세요~ 오늘은 비가 옵니다.</p>')

def insert(request):
    msg = ""
    # 줄바꿈 <br>
    
    # 1-linux 입력
    Curriculum.objects.create(name='linux')
    msg += "1-linux 입력 성공 <br>"
    # 2-python 입력
    c = Curriculum(name = 'python')
    c.save()
    msg += "python 입력 성공 <br>"
    # 3-html/css/js 입력
    Curriculum(name='3-html/css/js').save()
    msg += "3-html/css/js 입력 성공 <br>"
    # 4-django 입력
    Curriculum(name='django').save()
    
    return HttpResponse(msg + "django 입력 성공 <br>")

# 전체 조회
def show(request):
    data = Curriculum.objects.all()
    
    msg = ""
    for dt in data :
        msg += dt.name + '<br>'
        
    return HttpResponse(msg)

# 한건 조회
def oneshow(request):
    onedata = Curriculum.objects.get(pk=2)
    
    return HttpResponse(onedata.name)
