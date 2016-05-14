import sqlite3

db = "test.db"
def 아이템추가(번호: object, 음료명: object, 재고: object) -> object:
    print("함수 시작",db)
    with sqlite3.connect(db) as DB:
        print("DB연결")
        질의 = DB.cursor()
        print("커서 연결")
        질의.execute('INSERT INTO item (num,name,count) VALUES (번호,음료명,재고)')
        print("자료 추가")
        질의.commit()
        print("db 커밋")
        print("{1}을 {0}번에 추가하였습니다.".format(번호,음료명))


def 아이템조회():
    print("함수 시작",db)
    with sqlite3.connect(db) as DB:
        print("DB연결")
        질의 = DB.cursor()
        print("커서 연결")
        질의.execute("SELECT * FROM item")
        print("조회 완료")
        for row in 질의:
            print(row)

def 아이템조회():
    print("함수 시작", db)
        with sqlite3.connect(db) as DB:
        print("DB연결")
        질의 = DB.cursor()
        print("커서 연결")
        질의.execute("SELECT * FROM item")
                print("조회 완료")
                for row in 질의:
                    print(row)
#아이템추가(3,"헉개수",10)

#아이템 추가 함수 오류로 인한 확인용 구문
#DB의 연결 문제인지 insert 구문 오류인지 판단하기 위함
아이템조회()
