#여러줄 문자열
mulit_line = '''Life is short.
You need Python
And I need C#, too.
'''
print(mulit_line)

#리스트(배열)
b = [1,2,3,4]


print(b)

b.append(5) 
print(b)

b.insert(3, 10) #3번째자리에 10 삽입
print(b)

b.insert(3, 10) #원하는 인덱스에 추가
print(b)

b.sort() #오름차순 정렬
print(b)

b.reverse() #내림차순 정렬
print(b)

b.remove(10) #원소삭제

print(type(b))

##튜플 
c = (1,2,3,4)
print(c)
# c.append(5) 튜플에서는 값 추가 불가
print(c[2])

## 딕셔너리 key : vlaue 쌍의 집합
spiderman = {'name' : '피터 파커',
                      'age' : 18,
                      'weapon' : "웹슈터",
                      'memberOfAvengers' : True
                     }

print(spiderman)
print(spiderman['name'])
print(spiderman['memberOfAvengers'])
