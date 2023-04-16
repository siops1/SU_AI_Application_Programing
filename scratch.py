import time

class kiosk:
    __dict = {} #메뉴, 인덱스 저장
    __sel = 0
    __menu_list = {} #메뉴, 개수
    __menu_sum_list = {} #메뉴, 총합
    sum = 0;

    def menu_print(self):
        print('-'*25)
        print("\t SU SUMMER CAFE")
        print('-' * 25)
        inx = 1;
        for menu, cost in self.__dict.items():
            print("%d. %s\t\t%s원"%(inx, menu, cost))
            inx += 1
        print('-' * 25)
        if len(self.__menu_list) != 0:
            for i in self.__menu_list:
                print("%s"%i)
            print("총합 : %d원"%self.sum)

    def menu_dict(self, menu, cost):
        self.__dict[menu] = cost

    def menu_sum(self):
        while True:
            menu = list(self.__dict.keys())[self.__sel-1]
            cost = list(self.__dict.values())[self.__sel-1]
            print("%s은(는) %s원입니다"%(menu, cost))
            count = int(input("몇 개를 드릴까요? : "))
            print("%s은(는) %d원입니다."%(menu, cost * count))

            if menu in self.__menu_list:
                temp = self.__menu_list[menu]
                self.__menu_list[menu] = count + temp
            else:
                self.__menu_list[menu] = count

            plus_sel = input("더 주문하시겠습니까? (Y/N) : ")

            return plus_sel.lower()

    def menu_sel(self):
        self.__sel = int(input('메뉴를 선택해주세요(1~%d) : '%len(self.__dict)))

    def menu_list_up(self):
        sum = 0
        print('-'*25)
        for menu, count in self.__menu_list.items():
            print("%s\t%d\t%d"%(menu, count, self.__dict[menu] * count))
            sum = sum + self.__dict[menu] * count
        print('-' * 25)
        print("\t\t\t    %d"%sum)
kiosk_1 = kiosk()
kiosk_1.menu_dict('에스프레소', 4000)
kiosk_1.menu_dict('마끼아또', 4000)
kiosk_1.menu_dict('밀크파르페', 6500)
kiosk_1.menu_dict('아이스라떼', 4400)
order_num = 1

return_sel = 'y' \

kiosk_1.menu_print()
while True:
    if  return_sel == 'y':
        kiosk_1.menu_sel()
        return_sel = kiosk_1.menu_sum()
    else:
        kiosk_1.menu_list_up()
        break