import sqlite3
from libs.db.dba import getConn

def create_table():    # p03.py 이외에서 create_table()를 실행할 때 수행
    conn = getConn()     # db와 접속 정보
    cur = conn.cursor()    # db를 보는 포인터
    cur.execute('''
        create table test(name text, kor int, eng int, mat int)
        ''')
    conn.commit()
    conn.close()    # db와의 접속을 끊음

if __name__ == '__main__':    # p03.py 에서 create_table()를 실행할 때 수행
    create_table()