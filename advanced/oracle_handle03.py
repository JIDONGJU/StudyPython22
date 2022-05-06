# DB연동 - INSERT INTO

import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8')
    return conn

def get_list(conn):
    cur = conn.cursor()
    for row in cur.execute('SELECT * FROM divtbl'):
        print(row)

    cur.close()
    conn.close()

def set_list(conn, tup):
    cur = conn.cursor()
    query = f"INSERT INTO divtbl VALUES ('{tup[0]}', '{tup[1]}')" #SQL inject 보안문제+사용효율성
    cur.execute(query)
    conn.commit() # 완전 저장
    cur.close()
    conn.close()

if __name__ == '__main__':
    print('DIVTBL데이터 조회')
    get_list(myconn())
    print('DIVTBL 신규입력')
    division, names = input('(division, names) 입력 (구분자 \' \') > ').split(' ')
    tup = (division, names)
    set_list(myconn(), tup)

    print('입력 후 DIVTBL 데이터 조회')
    get_list(myconn())