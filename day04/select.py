import sqlite3
from libs.db.dba import getConn

def select_1():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('select * from test')
    rs = cur.fetchall()    # 모두 출력함
    for i in rs:
        print(i)
    conn.close()

def select_2():
    conn = getConn()
    cur = conn.cursor()
    cur.execute(' select * from test where name = "홍길동" ')
    rs = cur.fetchmany(2)    # 출력할 개수
    for i in rs:
        print(i)
    conn.close()

def select_3(name):
    conn = getConn()
    cur = conn.cursor()
    cur.execute('select * from test where name = ?', (name, ))
    rs = cur.fetchmany(1)
    for i in rs:
        print(i)
    conn.close()

if __name__ == '__main__':
    # select_1()
    # select_2()
    findname = input('이름 : ')
    select_3(findname)