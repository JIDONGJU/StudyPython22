from django.http import HttpResponse
from django.shortcuts import render
from .model_pandas import member as mem
from .model_pandas import cart
from .model_pandas import prod


# Create your views here.

def test(request):
    return render(
        request,
        "oracleapp/1.html",
        {}
    )

# 회원 전체조회
def view_memberlist(request):
    
    df = mem.getMemberList()
    # return HttpResponse(df)

    context = {'df':df}
    
    return render(
        request,
        "oracleapp/member_list.html",
        context
    )

# 회원 상세조회
def view_Member(request):
    df_dict = mem.getMember('a001')
    # context = {'df':df}
    # return HttpResponse(df_dict)
    return render(
        request,
        "oracleapp/member.html",
        df_dict
    )

# 장바구니 전체조회
def view_cart_list(request):

    df = cart.getCartList()
    # return HttpResponse(df)

    context = {'df':df}

    return render(
        request,
        "oracleapp/cart/cart_list.html",
        context
    )

# 장바구니 상세조회
def view_cart(request):
    df_dict = cart.getCart('r001')
    # context = {'df':df}
    # return HttpResponse(df_dict)
    return render(
        request,
        "oracleapp/cart/cart.html",
        df_dict
    )

def set_Cart_insert(request):
    id = 'e001'
    prod = 'P102000001'
    qty = 17
    
    msg = cart.setCartInsert(id,prod,qty)
    
    return HttpResponse(msg)

# 상품 전체조회
def view_lprod_list(request):

    df = prod.getLprodList()
    # return HttpResponse(df)

    context = {'df':df}

    return render(
        request,
        "oracleapp/prod/prod_list.html",
        context
    )