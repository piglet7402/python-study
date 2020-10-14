import sqlite3
from libs.db.dba import getConn

def insert_1():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('''
        insert into test values('홍길동', 60, 70, 80)
    ''')
    conn.commit()
    conn.close()

def insert_2():
    conn = getConn()
    cur = conn.cursor()
    ins_sql = 'insert into test values(?, ?, ?, ?)'    # 동적 쿼리
    cur.execute(ins_sql, ('김길동', 55, 61, 90))    # 튜플
    conn.commit()
    conn.close()

def insert_3():
    conn = getConn()
    cur = conn.cursor()
    li = [('김동길', 77, 88, 99), ('한우이',12, 99, 50), ('커피', 100, 10, 80)]
    ins_sql = 'insert into test values(?, ?, ?, ?)'    # 동적 쿼리
    cur.executemany(ins_sql, li)    # 리스트 내부구조는 튜플
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # insert_1()
    # insert_2()    # insert_2('김길동', 55, 61, 90)
    insert_3()