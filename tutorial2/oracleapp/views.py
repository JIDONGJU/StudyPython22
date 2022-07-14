from django.http import HttpResponse
from django.shortcuts import render
from .model_pandas import member as mem
from .model_pandas import cart
from .model_pandas import lprod

# Create your views here.
def test(request):
    
    return render(
        request,
        "oracleapp/test.html",
        {}
    )
    
# 회원전체 조회
def view_Member_List(request):
    
    df = mem.getMemberList()

    #return HttpResponse(df)

    context = {"df" : df}

    return render(
        request,
        "oracleapp/member_list.html",
        context
    )
    
# 회원 상세조회
def view_Member(request) :
    df_dict = mem.getMember("a001")
    
    #context = {"df" : df}
    
    #return HttpResponse(df_dict)

    return render(
        request,
        "oracleapp/member.html",
        df_dict
    )
    
    
# 주문내역 전체 조회(리스트+튜플 사용)
def view_Cart_List(request):
    
    df = cart.getCartList()

    #return HttpResponse(df)

    context = {"df" : df}

    return render(
        request,
        "oracleapp/cart/cart_list.html",
        context
    )

# 주문내역 전체 목록(리스트 + 딕셔너리 사용)
def view_Cart_List_dict(request):
    
    df_list = cart.getCartList()

    #return HttpResponse(df)

    context = {"df_list" : df_list}

    return render(
        request,
        "oracleapp/cart/cart_list_dict.html",
        context
    )
    
    
# 주문내역 상세조회(한건 조회)
def view_Cart(request) :
    cart_no = request.GET["cart_no"]
    cart_prod = request.GET["cart_prod"]
    
    df_dict = cart.getCart(cart_no, cart_prod)
    
    #context = {"df" : df}
    
    #return HttpResponse(df_dict)

    return render(
        request,
        "oracleapp/cart/cart.html",
        df_dict
    )

# 입력 처리    
def set_Cart_Insert(request):
    id = "e001"
    prod= "P102000001"
    qty = 17
    
    msg = cart.setCartInsert(id, prod, qty)
    
    return HttpResponse(msg)

# 삭제 처리
def set_Cart_Delete(request):
    cart_no = request.GET["cart_no"]
    cart_prod= request.GET["cart_prod"]
    
    msg = cart.setCartDelete(cart_no, cart_prod)
    
    return render(
        request,
        "oracleapp/cart/cart_delete.html",
        {"msg" : msg}
    )

# 수정 화면
def view_Cart_Update(request):
    pcart_no = request.GET["cart_no"]
    pcart_prod= request.GET["cart_prod"]
    
    df_dict = cart.getCart(pcart_no, pcart_prod)
    
    # context = {"pcart_no" : pcart_no,
    #             "pcart_prod" : pcart_prod}
    df_dict["pcart_no"] = pcart_no
    df_dict["pcart_prod"] = pcart_prod
    
    return render(
        request,
        "oracleapp/cart/cart_update_form.html",
        df_dict
    )
    
# 수정 처리
def set_Cart_Update(request):
    cart_no   = request.POST["cart_no"]
    cart_prod = request.POST["cart_prod"]
    cart_qty  = request.POST["cart_qty"]
    
    msg = cart.setCartUpdate(cart_no, cart_prod, cart_qty)
    
    pageControl = ""
    
    if msg =='Y':
        pageControl = """<script>
                        alert('수정 되었습니다!')
                        location.href='/oracle/cart_list_dict/'
                        </script>
        """
    
    else:
        pageControl = """<script>
                        alert('수정 실패!')
                        history.go(-1)
                        </script>
        """
    
    return HttpResponse(pageControl)
    # return render(
    #     request,
    #     "oracleapp/cart/cart_update.html",
    #     {"msg":msg}
    # )

# 리스트 + 튜플을 --> 리스트 + 딕셔너리로 전환 테스트
def testDict(request) :
    context = {"dt" : [{"no1":1,"no2":2,"no3":3},
                        {"no1":4,"no2":5,"no3":6}]}
    #return HttpResponse(context)
    return render(
        request,
        "oracleapp/cart/testdict.html",
        context
    )
    
# 상품분류 전체 조회    
def view_Lprod_List(request):
    
    df_list = lprod.getLprodList()

    #return HttpResponse(df)

    context = {"df_list" : df_list}

    return render(
        request,
        "oracleapp/lprod/lprod_list.html",
        context
    )
    
# 상품분류 상세조회
def view_Lprod(request) :
    
    lprod_gu = request.GET["lprod_gu"]
    
    df_dict = lprod.getLprod(lprod_gu)
    
    #context = {"df" : df}
    
    #return HttpResponse(df_dict)

    return render(
        request,
        "oracleapp/lprod/lprod.html",
        df_dict
    )
    
    