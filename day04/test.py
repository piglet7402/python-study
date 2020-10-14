import sqlite3
from libs.db.dba import getConn

class db:
    conn = getConn('d:/share/phone.db')
    cur = conn.cursor()
    def create_table(self):
        db.cur.execute('create table tel(name text, no text)')
    def insert_table(self):
        self.name = input("이름 : ")
        self.no = input("번호 : ")
        self.ist_sql = 'insert into tel values(?, ?)'
        db.cur.execute(self.ist_sql, (self.name, self.no))
    def select_table(self):
        self.sel_sql = "select * from tel"
        db.cur.execute(self.sel_sql)
        rs = db.cur.fetchall()
        print('==출력결과==')
        for k, v in rs:
            print(k, v)
    def update_table(self):
        # self.w1 = input("수정할 속성 : ")
        self.w2 = input("기존 값 : ")
        self.w3 = input("변경 값 : ")
        self.upt_sql = 'update tel set name = ? where name = ?'
        db.cur.execute(self.upt_sql, (self.w3, self.w2))
    def deltet_table(self):
        # self.d1 = input("삭제할 속성 : ")
        self.d2 = input("삭제할 값 : ")
        self.del_sql = 'delete from tel where name = ?'
        db.cur.execute(self.del_sql, (self.d2, ))
def main():
    tt = db()    # 실제 db를 위한 인스턴스 생성
    while True:
        n = input('a. 테이블 생성\t1. 입력\t2. 조회\t3. 수정\t4. 삭제\t5. 종료 : ')
        if n == 'a':
            tt.create_table()
        elif n == '1':
            tt.insert_table()
        elif n == '2':
            tt.select_table()
        elif n == '3':
            tt.update_table()
        elif n == '4':
            tt.deltet_table()
        elif n == '5':
            tt.conn.commit()
            tt.conn.close()
            break
    print('exit()')

if __name__ == '__main__':
    main()