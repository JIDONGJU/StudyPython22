# django 가상환경에서 cx_Oracle 설치해야 합니다.
# 설치 : 가상환경 프롬포트 > pip install cx_Oracle
import pandas
import cx_Oracle

# 오라클 연결 및 접속하기
def getConnection():
    # 오라클 연결하기
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    # 오라클 접속하기
    conn = cx_Oracle.connect(user='busan_06', password='dbdb', dsn=dsn)
    return conn

# 커서 받기
def getCursor(conn):
    cursor = conn.cursor()
    return cursor

# 접속 정보 및 커서 반납
def dbClose(cursor, conn):
    # 커서 반납 먼저
    cursor.close()
    # 마지막에 접속정보 반납
    conn.close()
    
###### <실제 사용하는 함수> ######

# 주문내역 전체 리스트 조회
def getCartList():
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """ SELECT * FROM cart """
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    # 컬럼명 조회하기
    colname = cursor.description
    col = []
    
    for i in colname:
        col.append(i[0])

    list_row = []
    
    for tup in row:
        dict_row = {}
        for i in range(0,len(tup),1):
            dict_row[col[i].lower()] = tup[i]
        list_row.append(dict_row)
        
    dbClose(cursor, conn)
    
    return list_row

# 한건 행에 대한 딕셔너리 만드는 함수
def getDictType_FetchOne(col_name, row_one):
    dict_row = {}
    
    for i in range(0, len(row_one), 1) :
        dict_row[col_name[i].lower()] = row_one[i]
    
    return dict_row


# 주문 상세조회 - 1건 조회
def getCart(no):
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """ Select * From cart
                Where cart_no = :cart_no"""
    cursor.execute(sql, cart_no=no)
    
    # 한 건 조회
    row = cursor.fetchone()
    
    # 컬럼명 조회하기
    colname = cursor.description
    col = []
    for i in colname:
        col.append(i[0])

    # 딕셔너리로 데이터 구성하기  
    dict_row = getDictType_FetchOne(col, row)
        
    dbClose(cursor, conn)
    
    return dict_row

# 주문내역 입력하기
def setCartInsert(id, prod, qty):
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문번호 생성을 위한 sql문 작성
    sql = """ Select DECODE(SUBSTR(max(cart_no),1,8),
                TO_CHAR(SYSDATE, 'YYYYMMDD') , max(cart_no) + 1,
                TO_CHAR(SYSDATE, 'YYYYMMDD') || '00001') as max_no
                From cart """
    cursor.execute(sql)
    
    # 한 건 조회
    max_no = cursor.fetchone()
    no = max_no[0]
    
    # 주문내역 입력을 위한 sql문 작성
    sql = """ Insert into cart(cart_no,cart_prod,cart_member,cart_qty)
                Values(:cart_no,:cart_prod,:cart_member,:cart_qty)"""
    cursor.execute(sql,
                    cart_no = no,
                    cart_prod = prod,
                    cart_member = id,
                    cart_qty = qty)
    conn.commit()
    dbClose(cursor, conn)
    
    return "입력성공..."

# 여러건에 대한 리스트 + 딕셔너리 만드는 함수
def getDictType_FetchAll(col_name, row):
    list_row = []
    dict_row = {}

    for tup in row:
        print(tup)
        
        for i in range(0,len(tup),1):
            print(tup[i])
            dict_row[col_name[i]] = tup[i]
        print(dict_row)
        list_row.append(dict_row)
        
    return list_row


# 주문내역 입력하기
def setCartDelete(no, prod):
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문내역 입력을 위한 sql문 작성
    sql = """ delete from cart
            where cart_no = :cart_no
            and cart_prod = :cart_prod"""
            
    cursor.execute(sql,
                    cart_no = no,
                    cart_prod = prod)
    
    conn.commit()
    
    dbClose(cursor, conn)
    
    return "삭제성공..."