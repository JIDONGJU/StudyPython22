# 주소록 프로그램 v1.0
# 작성일 : 2022-05-09
# 작성자 : 지동주
# 설   명 : 월요일 - 파일DB에서 Oracle로 변경

import os
from sqlite3 import connect
from turtle import Turtle
import cx_Oracle as ora

# 연락처 클래스
class Contact:
    name = ''; phone_num = ''; e_mail = ''; addr = ''

    def __init__(self, name, phone_num, e_mail, addr) -> None:
        self.name = name
        self.phone_num = phone_num
        self.e_mail = e_mail
        self.addr = addr

    def __str__(self) -> str:
        str_val = (f'이   름 : {self.name}\n'
                        f'핸드폰 : {self.phone_num}\n'
                        f'이메일 : {self.e_mail}\n'
                        f'주   소 : {self.addr}\n'
                        f'========================================'
                        )
        return str_val

def initDB():
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8')
    return conn

def run():
    list_contact = [] # 빈 리스트 생성
    conn = initDB() # 오라클 연결해서 연결객체 생성
    clearConsole()

    while True:
        sel_menu = get_menu()
        if sel_menu == 1: #연락처 추가
            clearConsole()
            isval =  set_contact(conn)
            if isval:
                input('연락처 추가성공\n계속하려면 엔터를 누르세요') # 아무값도 엔터 대기
            else:
                input('오류발생! 관리자 문의 요망')    
            clearConsole()
            continue # contact가 비면 리스트 추가 불가

        elif sel_menu == 2: #연락처 출력
            clearConsole()
            get_contact(list_contact)
            input('연락처 출력성공\n계속하려면 엔터를 누르세요') # 엔터 대기
            clearConsole()

        elif sel_menu == 3: #연락처 삭제
            clearConsole()
            name = input('삭제할 이름 입력 > ')
            del_contact(list_contact, name)
            input('연락처 삭제성공\n계속하려면 엔터를 누르세요')
            clearConsole()

        elif sel_menu == 4: # 종료
            save_contact(list_contact) # 파일DB저장
            break
        else:
            clearConsole()

#주소록 입력함수
def set_contact(conn):
    contact = None
    isSucceed = False # 입력 성공여부
    try: # 아무입력없이 엔터 | 갯수 틀리면 생기는 예외처리
        name, phone_num, e_mail, addr = \
        input('정보입력(이름, 핸드폰, 이메일, 주소(구분자 /))').split('/')
        contact = Contact(name, phone_num, e_mail, addr)
        #DB처리
        cur = conn.cursor()
        query = ('insert into addressbook ' #공백 없으면 오류발생
                     'VALUES (SEQ_ADDRBOOK.nextval, :1, :2, :3, :4)')
        tup = (contact.name, contact.phone_num, contact.e_mail, contact.addr)
        cur.execute(query, tup)
        conn.commit()
        cur.close()
        isSucceed = True

    except Exception as e:
        print('입력갯수를 확인(이름/핸드폰/이메일/주소)')
        isSucceed = False
    finally:
        return isSucceed # True면 DB입력성공, False면 실패

    return contact

#주소록 전체출력
def get_contact(list_contact):
    for contact in list_contact:
        print(contact)

#주소록 삭제
def del_contact(list_contact, name):
    for i, contact in enumerate(list_contact):
        if contact.name == name:
            del list_contact[i]


# 주소록 파일DB 저장
def save_contact(list_contact:list):
    f = open('./advanced/db_contact.txt', mode = 'w', encoding='utf-8')
    for contact in list_contact:
        f.write(contact.name + '/')
        f.write(contact.phone_num + '/')
        f.write(contact.e_mail + '/')
        f.write(contact.addr + '\n')

    f.close()



# 메뉴 출력 및 선택
def get_menu():
    str_menu = ('--주소록 프로그램 v1.1--\n'
                        '1. 연락처 추가\n'
                        '2. 연락처 출력\n'
                        '3. 연락처 삭제\n'
                        '4. 종료\n')
    print(str_menu)
    #0-9숫자 외에는 ValueError 발생
    menu = 0 # 초기화
    try:
        menu = int(input('메뉴입력 : '))
    except Exception as e:
        print(e)
    finally:
        return menu

def clearConsole():
    command = 'clear' #mac, unix, linux 화면클리어 명령어
    if os.name in ('nt', 'dos'):
        command = 'cls' #windows, dos 화면클리어 명령어
    os.system(command)

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt as e:
        print('Ctrl+c 종료')
    finally:
        pass
    print('--주소록 프로그램 v1.1--')
    run()