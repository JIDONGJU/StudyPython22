# 예외처리 1 - 예외발생
def multi(a, b):
    res = a * b
    return res

def divide(a, b):
    # if b == 0: return 0
    res = 0

    try:
        res = a / b
    except Exception as e :
        print(f'예외발생 {e}')
    finally:
        return res

value = 7
print('곱셈/나눗셈')

# try:
#     print(divide(6, 0))
    
# except ZeroDivisionError as e:
#     #print(e)
#     print('b에다가 0쫌 넣지 마세요!')

print(multi(6, 6))
print('종료')

if __name__ == '__main__':
    value = 7
    print('곱셈/나눗셈')
    print(divide(6, 0))
    print(multi(6, 6))
    print('종료')