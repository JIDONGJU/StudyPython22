from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from secondapp.models import Course
from .models import Course

def main(request):
    return HttpResponse('<u>Main</u>')

def insert(request):
    Course.objects.create(name='데이터 분석')
    Course.objects.create(name='데이터 수집')
    Course.objects.create(name='웹개발')
    Course.objects.create(name='인공지능')
    
    return HttpResponse('<u>데이터 입력 완료</u>')