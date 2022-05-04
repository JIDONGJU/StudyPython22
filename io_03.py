# 두개의 값을 입력받아 두개의 변수에 나눠담기

x, y, z = input('두 단어를 입력하세요(구분자는 /) > ').split('/')
print(x)
print(y)
print(z)

a, b = input('두 단어를 입력하세요(구분자는 /) > ').split('/') # 숫자 넣었을때
print(int(a) * int(b)) #여기서 int

a, b = map(int, input('두 단어를 입력하세요(구분자는 /) > ').split('/')) # map함수 사용한 정수형
print( a * b)

a, b = map(float, input('두 단어를 입력하세요(구분자는 /) > ').split('/')) # map함수 사용한 실수형
print( a / b)

greeting = "Hello, i'm teacher. \"Bye~\" "
print(greeting)