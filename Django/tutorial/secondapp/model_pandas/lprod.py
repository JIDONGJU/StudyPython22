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

# 상품구매 전체 리스트 조회
def getLprodList():
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """ SELECT * FROM LPROD """
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
def getDictType_FetchOne(col_name,row_one):
    dict_row = {}
    
    for i in range(0,len(row_one),1):
        dict_row[col_name[i].lower()] = row_one[i]
        
    return dict_row


# 상품구매 상세조회~1건조회
def getLprod(gu):
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """SELECT * FROM LPROD
            WHERE LPROD_GU = :LPROD_GU"""
    cursor.execute(sql, LPROD_GU=gu)
    
    row = cursor.fetchone()
    
    # 컬럼명 조회하기
    colname = cursor.description
    col = []
    for i in colname:
        col.append(i[0])
    
    dict_row = getDictType_FetchOne(col,row)
    
    dbClose(cursor, conn)
    
    return dict_row