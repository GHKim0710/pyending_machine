
# 간이 자판기 프로그램 입니다.
# 자판기에 들어가는 제품
사리다 = {"num": 1, "name": "사리다", "price": 800}
콤디션 = {"num": 2, "name": "콤디션", "price": 1500}
포가리 = {"num": 3, "name": "포가리", "price": 1000}
menu = [사리다 ,콤디션 ,포가리]

# ==========================
# 화면 출력을 위한 함수

def dp_menu():
    # 자판기 화면에서 메뉴 부분을 출력해주는 함수
    print("| 번호 |   제품명 |    가격 |")
    for can in menu:
        print("| {0:<4} | {1:>5} | {2:>5}원 |".format (can["num"] ,can["name"] ,can["price"]))

def dp():
    print("_____________________________")
    print("|   시원한 음료수 자판기    |")
    print("+======+==========+=========+")
    dp_menu()
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
        if coin > co_max:
            print("최대 5000원까지만 넣어주세요")
            continue
        elif coin < co_min:
            print("최소 {0}원보다 더 넣어주세요")
            continue
        else:
            break
    return coin

def can_list():
    # 제품의 숫자 목록을 반환하는 함수
    num_list = []
    for can in memu:
        num_list.append(can["number"])
    return num_list

def can():
    pass

def result():
    pass



dp()
coin()
