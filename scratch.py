import time

class KIOSK:
    __dict = {} #메뉴, 인덱스 저장
    __sel = 0
    __menu_list = {} #메뉴, 개수
    __menu_sum_list = {} #메뉴, 총합
    def file_read(self):
        with open("coffee.txt", 'r') as coffee_file:
            menu = coffee_file.read()
            lst = menu.split('\n')
        coffee_menu = {}
        for i in range(0, len(lst) - 1):
            a = lst[i].split(", ")
            self.__dict[a[0]] = int(a[1])
        coffee_file.close()

        with open("bread.txt", 'r') as bread_file:
            menu = bread_file.read()
            lst = menu.split('\n')
        bread_menu = {}
        for i in range(0, len(lst) - 1):
            a = lst[i].split(", ")
            self.__dict[a[0]] = int(a[1])
        bread_file.close()

        with open("icecream.txt", 'r') as icecream_file:
            menu = icecream_file.read()
            a = menu.split('\n')
        for i in range(0, len(lst) - 1):
            self.__dict[a[i]] = 3000

        icecream_file.close()
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
            print(f"{inx}. {menu} {cost:,}원")
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

#Main
kiosk = KIOSK()
kiosk.file_read()

while True:
    return_sel = 'y'
    kiosk.menu_print()
    while True:
        if  return_sel == 'y':
            kiosk.menu_sel()
            return_sel = kiosk.menu_order()
        else:
            kiosk.menu_list_up()
            break
    kiosk.kiosk_reset()
    time.sleep(3)
    print("\n\n\n")
