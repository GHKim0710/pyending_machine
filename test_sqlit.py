import sqlite3

db = "test.db"
def 아이템추가(번호: object, 음료명: object, 재고: object) -> object:
    print("함수 시작",db)
    with sqlite3.connect(db) as DB:
        print("DB연결")
        질의 = DB.cursor()
        print("커서 연결")
        질의.execute('INSERT INTO item(num,name,count) VALUES (번호,음료명,재고)')
        print("{1}을 {0}번에 추가하였습니다.".format(번호,음료명))

아이템추가(3,"헉개수",10)
