import mysql.connector

config = {
    'user':'root',
    'password':'123123',
    'host':'127.0.0.1',
    'database':'pythondb',
    'port':'3306'
}

def getConn():
    conn = mysql.connector.connect(**config)
    return conn

'''
def get_test(*con):    # 튜플을 받을 때는 *
    print(con)
get_test(1, 2, 3, 4)


def get_test(**con):    # dict 를 받을 때는 **
    print(con)
get_test(a=1, b=2, c=3, d=4)
'''