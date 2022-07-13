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
    
    member_id = request.GET["member_id"]
    
    df_dict = mem.getMember(member_id)
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
    
    cart_no = request.GET["cart_no"]
    
    df_dict = cart.getCart(cart_no)
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
    
def testDict(request):
    context = {"dt": [{"no1":1,"no2":2,"no3":3,},
                    {"no1":4,"no2":5,"no3":6}]}
    #return HttpResponse(context)
    return render(
        request,
        "oracleapp/cart/testdict.html",
        context
    )

def view_Cart_delete(request):
    cart_no = request.GET['cart_no']
    cart_prod = request.GET['cart_prod']
    
    msg = cart.setCartDelete(cart_no,cart_prod)
    
    return render(
        request,
        "oracleapp/cart/cart_delete.html",
        {"msg" : msg}
    )
    
def view_Cart_update(request):
    pcart_no = request.GET['cart_no']
    pcart_prod = request.GET['cart_prod']
    
    # msg = cart.setCartDelete(cart_no,cart_prod)
    
    context = {"pcart_no":pcart_no,
                "pcart_prod":pcart_prod}
    return render(
        request,
        "oracleapp/cart/cart_update_form.html",
        context
    )