# 객체지향
class car:
    number = '54라 9538'
    company = '현대자동차'
    gear_mode = 'Automatic'
    fuel = '휘발유'

    # Object --객체지향에선 다 조직도를 가지고 있음
    #   Exception -- 이거 막으면 하위 자동으로 막아짐
    #       ValueError
    #       IndexError
    #       ZeroDivisionError



    def setPower(self):
        print('시동을 겁니다.')

    def setPark(self):
        self.setGear('P')
        print('주차합니다')

    # R(후진), N(중립), P(주차), D(드라이브), S(스포츠)
    def setGear(self, gear:str):
        print(f'{gear}모드로 전환합니다')

    def accerator(self):
        print('엑셀을 밟습니다')
    
    def pushBreak(self):
        print('브레이크를 밟습니다')

if __name__ == '__main__':
    mycar = car()
    print(f'제조사는 {mycar.company} 입니다')
    mycar.setPower()
    mycar.setGear('D')
    mycar.accerator()
    mycar.pushBreak()
    mycar.setPark()