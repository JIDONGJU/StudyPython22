from django.shortcuts import render

# Create your views here.

def sample_01(request):
    return render(
        request,
        "frontendapp/01_sample.html",
        {}
    )
    
def index_01(request):
    return render(
        request,
        "frontendapp/index_01.html",
        {}
    )
    
def index_02(request):
    return render(
        request,
        "frontendapp/index_02_css.html",
        {}
    )
    
def index_03(request):
    return render(
        request,
        "frontendapp/index_03_css.html",
        {}
    )
    
def index_04(request):
    return render(
        request,
        "frontendapp/index_04_css.html",
        {}
    )
    
def index_05(request):
    return render(
        request,
        "frontendapp/index_05_css.html",
        {}
    )
    
def index_06(request):
    return render(
        request,
        "frontendapp/index_06_css.html",
        {}
    )