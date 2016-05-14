import sqlite3

db = "test.db"



'''
아이템 추가용 함수
-- 현재 insert에서의 문제로 작동 불가
--  sql명령어가 ""로 쌓여 있기에 변수가 대입되지 않은것으로 추론됨
--  실제로 책에선 플레이스 홀더를 통하여 대입을 하지 직접 변수를 넣지 않음
'''
def 아이템추가(번호, 음료명, 재고):
    print("함수 시작",db)
    with sqlite3.connect(db) as DB:
        print("DB연결")
        질의 = DB.cursor()
        print("커서 연결")
        질의.execute('INSERT INTO item (num, name, count) VALUES ({0},{2},{1})'.format(번호,재고,음료명))
        print("자료 추가")
        질의.commit()
        print("db 커밋")
        print("{1}을 {0}번에 추가하였습니다.".format(번호,음료명))

#조회 문구는 문제 없이 실행됨
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

아이템추가(3,"헉개수",10)

#아이템 추가 함수 오류로 인한 확인용 구문
#DB의 연결 문제인지 insert 구문 오류인지 판단하기 위함
아이템조회()
