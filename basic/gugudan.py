# 구구단 프로그램
# 2 x 1 = 2 ... 2 x 9 =18  x * y = xy
# 3 x 1 = 3 ... 3 x 9 = 27
#                     9 x 9 = 81

print('---구구단 프로그램---')

for x in range(2, 10):
    print(f'{x}단 시작')
    for y in range(1, 10):
        print(f'{x}x{y}={x*y:2d}', end = ' ')
    print() # 단마다 줄 맞추기 위해서