import sqlite3
from libs.db.dba import getConn

def delete_1():
    conn = getConn()
    cur = conn.cursor()
    del_sql = 'delete from test where kor <= ?'
    cur.execute(del_sql, (80, ))    # 1개 짜리 튜플은 반드시 콤마
    conn.commit()
    conn.close()

if __name__ == '__name__':
    delete_1()