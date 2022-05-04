# 주소록 프로그램 v1.0
# 작성일 : 2022-05-04
# 작성자 : 지동주
# 설   명 : 와, 내일 논다!

# 연락처 클래스
import os

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

def run():
    list_contact = [] # 빈 리스트 생성
    clearConsole()

    while True:
        sel_menu = get_menu()
        if sel_menu == 1: #연락처 추가
            clearConsole()
            contact = set_contact()
            list_contact.append(contact)
            input() # 아무값도 엔터 대기
            clearConsole()

        elif sel_menu == 2: #연락처 출력
            clearConsole()
            get_contact(list_contact)
            input() # 엔터 대기
            clearConsole()

        elif sel_menu == 3: #연락처 삭제
            clearConsole()
            name = input('삭제할 이름 입력 > ')
            del_contact(list_contact, name)
            input()
            clearConsole()

        elif sel_menu == 4:
            break
        else:
            clearConsole()

#주소록 입력함수
def set_contact() -> Contact:
    name, phone_num, e_mail, addr = \
        input('정보입력(이름, 핸드폰, 이메일, 주소(구분자 /))').split('/')
    contact = Contact(name, phone_num, e_mail, addr)
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

def get_menu():
    str_menu = ('--주소록 프로그램 v1.1--\n'
                        '1. 연락처 추가\n'
                        '2. 연락처 출력\n'
                        '3. 연락처 삭제\n'
                        '4. 종료\n')
    print(str_menu)
    menu = input('메뉴입력 : ')
    return int(menu)

def clearConsole():
    command = 'clear' #mac, unix, linux 화면클리어 명령어
    if os.name in ('nt', 'dos'):
        command = 'cls' #windows, dos 화면클리어 명령어
    os.system(command)

if __name__ == '__main__':
    print('--주소록 프로그램 v1.1--')
    run()