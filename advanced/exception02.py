# 예외처리 2 - 예외발생 2

x, y = map(int, input('두 수를 입력하세요 > ').split(' '))

print(f'x = {x}')
print(f'y = {y}')

try:
    z = x / y
    print(f'{x} / {y} = {z}')
# except TypeError as e:
#     print('형변환 하세요')
# except ZeroDivisionError as e:
#     print('두번째 수에 0은 넣지마세요')
except Exception as e:
    print(f'예외발생 {e}')

print('나누기 종료')


# F5 디버깅 시작 / 중단점까지 계속 진행하기
# Shift + F5 디버깅 중지
# F9 중단점 설정/해제
# F10 프로시저 단위로 실행(한 라인씩 진행)
# F11 한 단계씩 코드 실행(메서드 안으로 진행)
