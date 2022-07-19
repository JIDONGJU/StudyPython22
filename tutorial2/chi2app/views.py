from doctest import DocFileCase
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from .model_pandas import survey
# Create your views here.

def test(request):
    return render(
        request,
        "chi2app/test.html",
        {}
    )
    
# 주문내역 전체 조회(리스트+튜플 사용)
def view_Cart_List(request):
    
    df = survey.getCartList()

    #return HttpResponse(df)

    context = {"df" : df}

    return render(
        request,
        "chi2app/cart_list.html",
        context
    )
    
def createTable(request):
    survey.createTableSurvey()
    
    return HttpResponse("Create Ok")

# 설문 데이터 입력 테스트
def set_Survey_Insert_test(request):
    pgender = '여'
    page = 20
    pco_survey = "스타벅스"
    
    survey.setSurveyInsert(pgender, page, pco_survey)
    
    return HttpResponse("Insert OK")

# 설문 전체 조회하기
def view_Survey_List(request):
    
    df = survey.getSurveyList()
    
    # return HttpResponse(df.to_html())
    context = {"df" : df.to_html()}
    
    return render(
        request,
        "chi2app/list.html",
        context
    )
    
# 설문 참여하기 페이지 view
def view_Servey(request):
    return render(
        request,
        "survey.html",
        {}
    )
    
# 설문 데이터 입력
def set_Survey_Insert(request):
    pgender = request.POST.get("gender")
    page = request.POST.get("age")
    pco_survey = request.POST.get("co_survey")
    
    rs = survey.setSurveyInsert(pgender, page, pco_survey)
    
    msg = ""
    if rs == "OK":
        msg = """<script>
                alert('입력 성공.')
                location.href = '/chi2/list'
                </script>"""
                
    return HttpResponse(msg)