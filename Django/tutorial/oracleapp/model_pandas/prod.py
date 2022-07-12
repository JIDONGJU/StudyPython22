# 1. M 함수이름 getProdList
# 2. V view_prod_list()
# 3. T prod_list.html
# 4. urls에서 prod_list 만들고 2번 호출

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
def getLprodList():
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """ SELECT * FROM lprod """
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    dbClose(cursor, conn)
    
    return row
