import sqlite3

db = "test.db"
def 아이템추가(num,음료명,재고):
    with sqlite3.connect(db) as DB:
        질의 = DB.cursor()
        질의.execute('INSERT INTO item VALUES (num,음료명,재고)')
        print("{1}을 {0}번에 추가하였습니다.".format(num,음료명))

아이템추가(3,"헉개수",10)
