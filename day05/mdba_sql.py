from libs.db.mdba import getConn

# conn = getConn()
# print(conn)

def create_table():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('''
        create table pptest(
            name varchar(20),
            kor int,
            eng int,
            mat int)
    ''')
    conn.commit()
    conn.close()

def insert_table():
    conn = getConn()
    cur = conn.cursor()
    ins_sql = 'insert into pptest values(%s, %s, %s, %s)'
    cur.execute(ins_sql, ('스치니', 80, 50, 10))
    conn.commit()
    conn.close()

def select_table():
    conn = getConn()
    cur = conn.cursor()
    sel_sql = 'select * from pptest'
    cur.execute(sel_sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    # conn.commit()
    conn.close()

def select_table_2(name):
    conn = getConn()
    cur = conn.cursor()
    sel_sql = 'select * from pptest where name like %s'
    cur.execute(sel_sql, (name, ))
    rs = cur.fetchall()
    display(rs)
    # print(rs)
    # conn.commit()
    conn.close()

def update_table(name, kor_jum):
    conn = getConn()
    cur = conn.cursor()
    upt_sql = 'update pptest set kor = %s where name = %s'
    cur.execute(upt_sql, (kor_jum, name))
    conn.commit()
    conn.close()

def delete_table(name):
    conn = getConn()
    cur = conn.cursor()
    del_sql = 'delete from pptest where name = %s'
    cur.execute(del_sql, (name, ))
    conn.commit()
    conn.close()

def display(rs):
    for j in rs:
        print('이름 :', j[0])
        tot = j[1] + j[2] + j[3]
        print('총점 :', tot)

'''
    for i, j in enumerate(rs):
        # print(i, j)
        print('이름 :', j[0])
        tot = j[1] + j[2] + j[3]
        print('총점 :', tot)
'''

'''
    index = 0
    for i in rs:
        print('이름 :', rs[index][0])
        tot = rs[index][1] + rs[index][2] + rs[index][3]
        print('총점 :', tot)
        index += 1
'''

if __name__ == '__main__':
    # create_table()
    # insert_table()
    # select_table()
    # select_table_2('홍길동')
    update_table('김길동', 100)
    delete_table('스치니')