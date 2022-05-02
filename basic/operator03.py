# 문자열 포맷팅
from asyncio import futures


name = '지동주'
login_str = '{0}님 로그인중'.format(name)
print(login_str)

# 문자열 포맷팅
print('{0}, {1}, {2}'.format('하나', 2, True))
print(f"{'하나'}, {2}, {True}")

# 소수점 표현
PI = 3.14159268
print('{0:0.2f}'.format(PI))
print(f'{PI:0.3f}')

full_name = 'DONGJU JI'
print(full_name.split()) # 리스트로 만들어버림
sp_name = full_name.split()
print(sp_name)
print(sp_name[0])

greeting = 'Hello, World'
words = greeting.split(',') # 문자열을 ,로 잘라서 리스트로
print(words)

hi = '             Hello~        '
print(hi.lstrip()) # oracle LTRIM() 오른쪽 공백 삭제
print(hi.rstrip()) # RTRIM 왼쪽 공백 삭제
print(hi.strip()) # TRIM 양쪽 공백 삭제

# 문자열 특정 단어, 문자열 값 변경
print(full_name.replace('DONGJU', 'messi'))

# 리스트 연산
arr = [1, 2, 3, 4, 5]

print(arr[3] + arr[0]) # 그냥 더하기 5

arr1 = ['1', 2, 3, '4', 5]

print(arr1[3] + arr1[0]) # 문자+문자는 가능 문자+숫자는 불가능
print(arr1[3] * arr1[2]) # 문자4를 3번 반복 출력

# 이중리스트
arr2 = [1, 2, 3.14, ['Hi', 'My', 'Friends']] # 2차원 배열
print(arr2[2]) # 3.14
print(arr2[3]) # ['Hi', 'My', 'Friends']
print(arr2[3][1]) # My
print(arr2[3][1][0]) # M

arr3 = arr + arr2
print(arr3)
