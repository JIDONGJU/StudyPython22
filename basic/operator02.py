# 문자열 연산
first = 'Hello'
second = 'World!'

print(first + second) #문자연산 + (합치기)
print(first, second) #CONCAT과 동일

print(first * 3) #문자열연산 +,* 밖에 없음

# 문자열 길이 내장함수
print(len('한글'))
print(len(first))

# 리스트 연산
print(first[0]) # [0]번째 문자 출력, 초과하면 에러

print(first[-1]) # 맨 뒤에서부터 -1 o
print(first[-2]) # 맨 뒤에서부터 -2 l
print(first[-3]) # 맨 뒤에서부터 -3 l
print(first[-4]) # 맨 뒤에서부터 -4 e
print(first[-5]) # 맨 뒤에서부터 -5 H
print(first[-6]) # 범위초과 에러

## 현재일시
current_date = '2022-05-02 14:24:15'
year = current_date[:4]
month = current_date[5:7]
day = current_date[8:10]
hour = current_date[11:13]
min = current_date[14:16]
sec = current_date[17:19]

print(year, '년:', month, '월:',day, '일:')
print(hour, '시:', min, '분:', sec, '초:')

print(current_date[-2:])

a = [1,2,3,4,5]
a[0] = 10
print(a)

p = 'python'
print(p)
p[0] = 'P' #Python으로 안됌 TypeError
p2 = ('P' + p[1:]) # 혹은 print('P' + p[1:])
print(p2)

print(p.upper()) #대문자변환
print(p2.lower()) #소문자변환