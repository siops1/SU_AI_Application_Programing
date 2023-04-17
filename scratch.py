import time

class kiosk:
    __dict = {} #메뉴, 인덱스 저장
    __sel = 0
    __menu_list = {} #메뉴, 개수
    __menu_sum_list = {} #메뉴, 총합

    def menu_dict(self, menu, cost): #딕셔너리에 메뉴 추가
        self.__dict[menu] = cost

    def menu_sel(self): #주문할 메뉴 입력
        self.__sel = int(input('메뉴를 선택해주세요(1~%d) : ' % len(self.__dict)))

    def kiosk_reset(self):
        self.__sel = 0
        self.__menu_list = {}
        self.__menu_sum_list = {}

    def menu_print(self): #메뉴 출력
        print('-'*25)
        print("\t SU SUMMER CAFE")
        print('-' * 25)
        inx = 1
        for menu, cost in self.__dict.items():
            print(f"%d. %s\t\t{cost:,}원"%(inx, menu))
            inx += 1
        print('-' * 25)

    def menu_order(self): #주문 처리
        while True:
            menu = list(self.__dict.keys())[self.__sel-1]
            cost = list(self.__dict.values())[self.__sel-1]
            print(f"%s은(는) {cost:,}원입니다"%menu)
            count = int(input("몇 개를 드릴까요? : "))
            print(f"%s은(는) {cost * count:,}원입니다."%menu)

            if menu in self.__menu_list:
                temp = self.__menu_list[menu]
                self.__menu_list[menu] = count + temp
            else:
                self.__menu_list[menu] = count

            plus_sel = input("더 주문하시겠습니까? (Y/N) : ")

            return plus_sel.lower()

    def menu_list_up(self): #최종 주문 내역 출력
        list_sum = 0
        print('-'*25)
        for menu, count in self.__menu_list.items():
            print(f"%s\t%d\t{self.__dict[menu] * count:,}"%(menu, count))
            list_sum = list_sum + self.__dict[menu] * count
        print('-' * 25)
        print(f"총합\t\t        {list_sum:,}")

kiosk_1 = kiosk()
#추후 파일 입출력 방식으로 변환
kiosk_1.menu_dict('에스프레소', 4000)
kiosk_1.menu_dict('마끼아또', 4000)
kiosk_1.menu_dict('밀크파르페', 6500)
kiosk_1.menu_dict('아이스라떼', 4400)
while True:
    return_sel = 'y'
    kiosk_1.menu_print()
    while True:
        if  return_sel == 'y':
            kiosk_1.menu_sel()
            return_sel = kiosk_1.menu_order()
        else:
            kiosk_1.menu_list_up()
            break
    kiosk_1.kiosk_reset()
    time.sleep(3)
    print("\n\n\n")
