

#간이 자판기 프로그램 입니다.
in_money = 0 # 자판기에 입력된 금액


def DP_menu(num,name,price):
    """
    자판기 디스플레이의 제품 출력 함수
    :param num: 제품 번호
    :param name: 제품 명
    :param price: 제품 가격
    :return:
    """
    print("{}.{} : {}원".format(num,name,price))


def display():
    # [] 추후 자판기에 등록된 제품을 넘겨받아 디스플레이에 뿌려주도록 수정
    print("_________________________")
    print("=========================")
    DP_menu(1,"사이다",1000)
    DP_menu(2, "콜라", 1050)
    DP_menu(3, "포카리", 1200)
    DP_menu(4, "이프로", 1500)
    print("=========================")
    print("-------------------------")

def input_money():
    """
    자판기에서 금액을 입력 받은후 입력된 금액이 올바른 값인지 검수후 입력값을 리턴
    :return: 자판기에 입력된 값
    """

    print("금액은 50원,100원,500원,1000원 단위로 입력가능하며 최대 5000원 까지 입력가능합니다")
    while 1 == 1:
        money = input("금액을 입력하세요")

        #입력값 검수
        # [] for값으로 검수를 하도록 수정
        #현제 문구는 제대로 작동되기 힘듦
        if money in "." :
            print("숫자만 입력하세요")
            continue
        elif int(money) > 5000:
            print("너무 많은 금액을 입력했습니다 5000원 이하로 입력하세요")
            continue
        elif money[-1] != 0 and money[-2] not in ["0","5"]:
            print("50원,100원, 500원, 1000원 단위로 입력가능합니다")
            continue

        return money



display()
in_money = input_money()
print(in_money)