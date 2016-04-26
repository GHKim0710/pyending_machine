

#간이 자판기 프로그램 입니다.

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


display()