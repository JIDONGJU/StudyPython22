from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from secondapp.models import Course
from .models import Course
from .model_pandas import lprod

def main(request):
    return HttpResponse('<u>Main</u>')

def insert(request):
    Course.objects.create(name='데이터 분석')
    Course.objects.create(name='데이터 수집')
    Course.objects.create(name='웹개발')
    Course.objects.create(name='인공지능')
    
    return HttpResponse('<u>데이터 입력 완료</u>')

# 회원 전체조회
def view_Lprod_list(request):
    
    df = lprod.getLprodList()
    # return HttpResponse(df)

    context = {'df':df}
    
    return render(
        request,
        "secondapp/lprod_list.html",
        context
    )

# 회원 상세조회
def view_Lprod(request):
    
    lprod_gu = request.GET["lprod_gu"]
    
    df_dict = lprod.getLprod(lprod_gu)
    # context = {'df':df}
    # return HttpResponse(df_dict)
    return render(
        request,
        "secondapp/lprod.html",
        df_dict
    )