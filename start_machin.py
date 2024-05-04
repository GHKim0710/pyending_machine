
# 간이 자판기 프로그램 입니다.
# 자판기에 들어가는 제품
사리다 = {"num": 1, "name": "사리다", "price": 800}
콤디션 = {"num": 2, "name": "콤디션", "price": 1500}
포가리 = {"num": 3, "name": "포가리", "price": 1000}
menu = [사리다 ,콤디션 ,포가리]
# ------------------------------
# ==========================
# 화면 출력을 위한 함수

def dp_menu(mode=0,coin=0):
    '''

    :param mode: 0 = 제품 전체 출력, 1 = 구입가능한 제품만 출력
    :param coin: 자판기에 들어간 돈
    :return:
    '''
    #제품 전체 출력
    if mode == 0:
        print("| 번호 |   제품명 |    가격 |")
        for can in menu:
            print("| {0:<4} | {1:>5} | {2:>5}원 |".format (can["num"] ,can["name"] ,can["price"]))
    elif mode == 1:
        memu_buy = []
        #구매 가능한 제품만 추리기
        for can in menu:
            if can["price"] <= coin:
                memu_buy.append(can)
        for can in memu_buy:
            print("| {0:<4} | {1:>5} | {2:>5}원 |".format(can["num"], can["name"], can["price"]))

def dp(mode=0,coin = 0):
    print("_____________________________")
    print("|   시원한 음료수 자판기    |")
    print("+======+==========+=========+")
    dp_menu(mode,coin)
    print("+======+==========+=========+")
    print("-----------------------------")


# ==================================
# 제품 선택 및 잔돈 처리를 위한 함수

def coin_min():
    # 자판기에 있는 제품가격중 최소값을 구하는 함수
    price_min = 0
    for can in menu:
        if price_min == 0 or can["price"] < price_min:
            price_min = can["price"]
    return price_min

def coin():
    # 투입 가능한 돈의 최대,최소 값
    co_min = coin_min()
    co_max = 5000
    # 돈을 입력받고 오류를 검증
    while True:
        coin = input("돈을 넣어주세요 :")
        try:
            coin = int(coin)
        except:
            print("숫자만 입력해주세요")
            continue
        if co_min > coin or coin > co_max:
            print("최소 {0}원, 최대 {1}원까지만 넣어주세요".format(co_min,co_max))
            continue
        else:
            break
    return coin

def num_list() -> object:
    # 제품의 숫자 목록을 반환하는 함수
    num_list = []
    for can in menu:
        num_list.append(can["num"])
    return num_list

# 원하는 제품 번호의 제품명을 알려주는 함수
def can_find(num):
    for i in menu:
        if num == i["num"]:
            return i


def can(coin):
    list = num_list()
    while True:
        dp(1,coin)  #구매 가능한 제품만 출력
        can = input("원하는 제품의 숫자를 입력해주세요")
        try:
            can = int(can)
        except:
            print("숫자만 입력해주세요")
            continue
        if can not in list: #메뉴에 있지 않은 제품 입력시
            print("{0}중 하나를 선택해 주세요".format(list))
            continue
        elif can_find(can)["price"] > coin: # 제품을 구매 할수 있는지 검증
            print("{0}원 보다 낮은 제품을 선택해주세요".format(coin))
            continue
        else:
            break
    name = can_find(can)["name"]
    price = can_find(can)["price"]
    change = coin-price
    print("{0}을 드렸습니다. 거스름돈은 {1}원 입니다.".format(name,change))

#프로그램 시작
dp()
coin = coin()
can(coin)