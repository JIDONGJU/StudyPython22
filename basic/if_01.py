# if문
name = '홍길동'
gender = '남'

if name == '홍길동':
    print('진료실로 들어갑니다.')
    print('의사쌤한테 인사합니다.')
else:
    print('부를때까지 기다리세요.')
    print('궁시렁거립니다.')

if name == '홍길동':
    if gender == '여':
        print('진료실로 들어갑니다.')
        print('의사쌤한테 인사합니다.')
    else:
        print('부를때까지 기다리세요.')
        print('궁시렁거립니다.')

if name == '홍길동' or  gender == '여':
    print('진료실로 들어갑니다.')
    print('의사쌤한테 인사합니다.')
else:
    print('부를때까지 기다리세요.')
    print('궁시렁거립니다.')

    num = 10

    if num != 9:
        print('9가 아닙니다.')
    else:
        print('9입니다')