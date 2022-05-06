# 오라클 DB 연동
import cx_Oracle as ora

# 데이터소스 네임 객체 생성 ( 접속주소, 포트번호, 서비스명)
dsn = ora.makedsn('localhost', 1521, sevice_name='orcl')
# DB연결객체
conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8')

cur = conn.cursor() # 
query = 'SELECT * FROM memberTBL'

for row in cur.execute(query):
    print(row)

cur.close()
conn.close()