import sqlite3
from libs.db.dba import getConn

def update_1(new_name, old_name):
    conn = getConn()
    cur = conn.cursor()
    upt_sql = "update test set name=? where name=?"
    cur.execute(upt_sql, (new_name, old_name))    #동적쿼리는 큐플 형태
    conn.commit()
    conn.close()

if __name__ == '__name__':
    update_1("김김김", "홍길동")